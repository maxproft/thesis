import FortranCGLE as cgle
import numpy as np


spacialpixels=6
mylist=np.complex64([(x+x*1j)/10 for x in range(spacialpixels)])
#print mylist
#mylist=np.complex64([1 for x in range(spacialpixels)])

comp1=np.complex64((1+2*1j)*0.01)
comp2=np.complex64((3+4*1j)*0.01)
comp3=np.complex64((5+6*1j)*0.01)
comp4=np.complex64((7+8*1j)*0.01)
delta = np.float32(0.9)
tottime = np.int32(10)
RealLength = np.float32(10.)
timestep = np.float32(0.1)

#print comp1,comp2
#print cgle.nonlinde(comp1,comp2,mylist)
#print cgle.nonlinear(0.1, comp1,comp2,mylist)


import FortranCGLE as cgle2
import pythonCGLE as cgle
#print cgle.nonlinear(0.1,1,1,mylist) - cgle2.nonlinear(0.1,1,1,mylist)
print cgle.alltime(timestep,tottime,comp1,comp2,comp3,comp4,RealLength,mylist)- cgle2.alltime(timestep,tottime,comp1,comp2,comp3,comp4,RealLength,mylist)

