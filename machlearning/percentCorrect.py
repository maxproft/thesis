from oct2py import octave
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Setting up octave
dir_path = os.path.dirname(os.path.realpath(__file__))
octave.addpath(dir_path)


#To test if the polynomial features are loading correctly
#a = [2,3,5]
#polytest = [a for i in range(10)]
#polyfeat = octave.polyFeatures(polytest)


#Loading the data from the machine learning algorithm so we can make predictions.
machInfo = np.loadtxt("trainingInfo.csv",delimiter=',')
theta = machInfo[0]
regMean = machInfo[1]
regSD = machInfo[2]

#Loading the data
initialdata = np.loadtxt('maxSD machLearnData.csv', delimiter= ',')
xdata = initialdata[:,:-1]
ydata = initialdata[:,-1]
print("Data Loaded, Making Poly Terms")
#Making polynomial features
polyfeat = octave.polyFeatures(xdata)
N,L = np.shape(polyfeat)
print("Num Poly Features: "+ str(L))

#Turning mean and SD into arrays for faster performance
meanArray = np.outer(np.array([1 for i in range(N)]),regMean)
SDArray = np.outer(np.array([1 for i in range(N)]),regSD)

#normalising the polynomial features
regPoly = np.divide(np.subtract(polyfeat,meanArray),SDArray)
regPoly[:,0]=1
#prediction of each data point
pred = np.dot(regPoly,theta)

PercentError = np.abs(np.divide(np.subtract(ydata, pred),ydata)*100)

a=0
for i in PercentError:
    if i<100:
        a+=1
print(int(a*100/N))

axes = plt.gca()
axes.set_ylim([0,400])
plt.hist(PercentError,bins=100,range=(0,100))
plt.show()








