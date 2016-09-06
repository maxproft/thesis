import random
import numpy as np


def rand():
    return random.random()

data = []

for i in range(10):
    for j in range(10):
        data.append([rand(),rand(),i,j,rand(),rand(),0.5+i+j**3])
print np.shape(data)

np.savetxt("data.csv", data, delimiter=",")
