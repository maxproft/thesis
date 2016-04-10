import FortranCGLE as cgle
import numpy as np


spacialpixels=7
mylist=np.complex64([(x+x*1j)/10 for x in range(spacialpixels)])
#mylist=np.complex64([1 for x in range(spacialpixels)])

comp1=np.complex64((1+2*1j)*0.01)
comp2=np.complex64((3+4*1j)*0.01)
comp3=np.complex64((5+6*1j)*0.01)
comp4=np.complex64((7+8*1j)*0.01)
delta = np.float32(0.9)
length = np.int32(5)
RealLength = np.float32(10.)


#a = cgle.fftinv(cgle.fft(mylist))
#b = cgle.fftinvfft(mylist)
#print a-b

#for x in range(10):
#    print cgle.fftinv(cgle.fft(mylist)) - cgle.fftinvfft(mylist)

#print cgle.arr2arr(2,mylist)
#print cgle.arr2arr(2,mylist)

print cgle.fft(mylist) - np.fft.fft(mylist)
print cgle.fftinv(mylist) - np.fft.ifft(mylist)



#testing inverse fourier transform does that
#print mylist
#print cgle.fft(cgle.fftinv(mylist))
#print cgle.fftinv(cgle.fft(mylist))

#print cgle.nonlinear(delta,comp3,comp4,mylist)
#print cgle.nonlinear(delta,comp3,comp4,mylist)

#for x in range(10):
    #a= cgle.alltime(delta,length,comp1,comp2,comp3,comp4,RealLength,mylist)
    #b= cgle.alltime(delta,length,comp1,comp2,comp3,comp4,RealLength,mylist)
    #print a
    #print b
    #print a-b

#print (delta,length,comp1,comp2,comp3,comp4,mylist)




if 0:
    nonlin = cgle.nonlinear(delta,comp3,comp4,mylist)
    nonlinfourier = cgle.fft(nonlin)
    temp = np.complex64([nonlinfourier[k]*np.exp(-comp2*delta*(k**2)*3.14159**2/float(spacialpixels)**2+comp1*delta) for k in range(len(nonlinfourier))])
    spacial = cgle.fftinv(temp)
    a= spacial
    b= cgle.alltime(delta,length,comp1,comp2,comp3,comp4,RealLength,mylist)[1] #the [1] is so we get the first time step.
    print a-b


