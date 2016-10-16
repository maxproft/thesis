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




#the reange of the x parameter and y parameter
xpixel = 100
ypixel = 100
xmin = -1.1
xmax = -0.4
ymin = 0
ymax = 2


#This is where I choose which parameters I keep constant
#delta(0),beta(1),D(2),epsilon(3),mu(4),nu(5),OTHER,(6)
testpoints = np.array([[-0.1,0.125,1,y,-0.1,x] for x in np.linspace(xmin,xmax,xpixel) for y in np.linspace(ymin,ymax,ypixel)])



#Making polynomial features
polyfeat = octave.polyFeatures(testpoints)
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
#turning the data from a list to an array
data = np.transpose([pred[i*ypixel:(i+1)*ypixel] for i in range(xpixel)])



#Plotting the datas
fig = plt.figure()
ax = fig.add_subplot(111)
cmap = cm.get_cmap('hot_r')
cs = plt.pcolor(data, cmap = cmap)
cb = plt.colorbar(cs, orientation='vertical')
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title")
plt.xticks(np.linspace(0,xpixel,5),np.linspace(xmin,xmax,5))
plt.yticks(np.linspace(0,ypixel,5),np.linspace(ymin,ymax,5))
plt.show()
