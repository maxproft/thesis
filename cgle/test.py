import FortranCGLE as cgle
import numpy as np


length=10
mylist=np.complex64([(x+x*1j)/10 for x in range(length)])
comp1=(1+3*1j)*0.1
comp2=(6+7*1j)*0.1
comp3=(4+5*1j)*0.1
comp4=(3+6*1j)*0.1
delta = 9

#print cgle.cgle.arr2arr(2,mylist)
#print cgle.cgle.arr2arr(2,mylist)

#print cgle.cgle.fft(mylist)
#print cgle.cgle.fft(mylist)

#print cgle.cgle.fftinv(mylist)
#print cgle.cgle.fftinv(mylist)

#testing inverse fourier transform does that
#print mylist
#print cgle.cgle.fft(cgle.cgle.fftinv(mylist))
#print cgle.cgle.fftinv(cgle.cgle.fft(mylist))

#print cgle.cgle.nonlinear(delta,comp3,comp4,mylist)
#print cgle.cgle.nonlinear(delta,comp3,comp4,mylist)

print cgle.cgle.nextstep(delta,3,comp1,comp2,comp3,comp4,mylist)
print cgle.cgle.nextstep(delta,3,comp1,comp2,comp3,comp4,mylist)


