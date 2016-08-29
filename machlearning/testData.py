import random
import numpy as np

#This gives random data
data = [[random.random()*(i+1) for i in range(7)] for j in range(50)]

np.savetxt("data.csv", data, delimiter=",")

#The data is in the form, ABCDEF, Height difference
