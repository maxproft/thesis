import FortranCGLE as cgle
import numpy as np



length=10
mylist=np.complex64([(x+x*1j)/100 for x in range(length)])
comp1=(1+3*1j)*0.001
comp2=(6+7*1j)*0.001
comp3=(4+5*1j)*0.001
comp4=(3+6*1j)*0.001
delta = 0.002
print cgle.cgle.arr2arr(2,mylist)
print cgle.cgle.fft(mylist)
print cgle.cgle.nonlinear(delta,comp3,comp4,mylist)
print cgle.cgle.nextstep(delta,5,comp1,comp2,comp3,comp4,mylist)

