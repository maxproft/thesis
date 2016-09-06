import random
import numpy as np

#This gives random data
data = [[random.random()*(i+1) for i in range(7)] for j in range(500)]

#This gives linear in one variable
def onelin(i,j):
    if i==3:
        return j*1
    elif i==6:
        return 3.1*j+1
    else:
        return random.random()
data = [[onelin(i,j) for i in range(7)] for j in range(500)]
print np.shape(data)

#This gives a quardratic in one variable
def quad(i,j):
    if i==3:
        return j*1.0
    elif i==6:
        return 1.*j**2
    else:
        return random.random()
#data = [[quad(i,j) for i in range(7)] for j in range(5000)]


np.savetxt("data.csv", data, delimiter=",")

#The data is in the form, ABCDEF, Height difference
