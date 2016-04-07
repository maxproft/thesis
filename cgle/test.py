import FortranCGLE as cgle
import numpy as np


spacialpixels=7
mylist=np.complex64([(x+x*1j)/10 for x in range(spacialpixels)])
#mylist=np.complex64([1 for x in range(spacialpixels)])

comp1=np.complex64((1+2*1j)*0.1)
comp2=np.complex64((3+4*1j)*0.1)
comp3=np.complex64((5+6*1j)*0.1)
comp4=np.complex64((7+8*1j)*0.1)
delta = np.float32(0.9)
length = np.int32(3)



#a= cgle.cgle.fftinv(cgle.cgle.fft(mylist))
#b= cgle.cgle.fftinvfft(mylist)
#print a-b


for x in range(10):
    print cgle.fftinv(cgle.fft(mylist)) - cgle.fftinvfft(mylist)



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

#a= cgle.cgle.nextstep(delta,length,comp1,comp2,comp3,comp4,mylist)
#b= cgle.cgle.nextstep(delta,length,comp1,comp2,comp3,comp4,mylist)
#print a
#print b
#print a-b

#print (delta,length,comp1,comp2,comp3,comp4,mylist)
#print cgle.cgle.test(delta,length,comp1,comp2,comp3,comp4,mylist)

#nonlin = cgle.cgle.nonlinear(delta,comp3,comp4,mylist)
#nonlinfourier = cgle.cgle.fft(nonlin)
#temp = [nonlinfourier[k]*np.exp(-comp2*delta*3.14159**2/spacialpixels**2+comp1*delta) for k in range(len(nonlinfourier))]
#spacial = cgle.cgle.fftinv(temp)
#print spacial


