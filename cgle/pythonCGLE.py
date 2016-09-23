import numpy as np
import pyfftw

def nonlinde(C,D,oldstate,absol,cterm,dterm,kn):
        np.conj(oldstate,absol)
        np.multiply(oldstate,absol,absol)#The conjugate
        np.multiply(absol, oldstate, cterm)
        np.multiply(cterm,absol,dterm)
        np.multiply(cterm, C,cterm)#all of the C term 
        np.multiply(dterm,D,dterm)#all of the D term
        np.add(cterm,dterm,kn)
        
        #absolute = oldstate * oldstate.conjugate()#These steps is what I did before.
        #return C*oldstate*absolute + D*oldstate*absolute**2

def nonlinear(C,D,oldstate,k1,k2,k3,k4,ksum,absol,cterm,dterm):
#Doing this allowed me to save ~0.5sec, so I might as well leave it here.
    nonlinde(C,D,oldstate,absol,cterm,dterm,k1)#k1
    np.multiply(k1,0.5,ksum)
    np.add(oldstate,ksum,ksum)
    nonlinde(C,D,ksum,absol,cterm,dterm,k2)#k2
    np.multiply(k2,0.5,ksum)
    np.add(k2,oldstate,ksum)
    nonlinde(C,D,ksum,absol,cterm,dterm,k3)#k4
    np.add(k2,oldstate,ksum)
    nonlinde(C,D,ksum,absol,cterm,dterm,k4)#k4
    #The code above is the same as this, but below is a bit easier to read:
    #nonlinde(C,D,oldstate,absol,cterm,dterm,k1)
    #nonlinde(C,D,oldstate+k1*0.5,absol,cterm,dterm,k2)
    #nonlinde(C,D,oldstate+k2*0.5,absol,cterm,dterm,k3)
    #nonlinde(C,D,oldstate+k3,absol,cterm,dterm,k4)

    np.add(k1,k4,k1)
    np.add(k2,k3,k2)
    np.multiply(k2,2,k2)
    np.add(k2,k1,k1)
    np.multiply(k1,1/6.,k1)
    np.add(k1,oldstate,oldstate)
    #return oldstate+(k1+2*k2+2*k3+k4)/6.#The same as above, but a bit faster

def newgenerator(timestep,A,B,C,D,RealLength,initial_state): #This finds the fastest FFT method once, and uses this many times.
        xSteps = len(initial_state)
        current_state = pyfftw.empty_aligned(xSteps, dtype='complex128')#n_byte_align_empty
        fourier_state = pyfftw.empty_aligned(xSteps, dtype='complex128')
        fft_object = pyfftw.FFTW(current_state, fourier_state)
        ifft_object = pyfftw.FFTW(fourier_state, current_state, direction='FFTW_BACKWARD')
        
        current_state[:] = initial_state
        
        LinList = pyfftw.empty_aligned(xSteps, dtype='complex128')
        LinList[:] = np.array([np.exp((A-B*(np.pi*(2*m-xSteps)/RealLength)**2)*timestep) for m in range(xSteps)])
        pm = pyfftw.empty_aligned(xSteps, dtype='complex128')
        pm[:] = np.array([(-1)**m for m in range(xSteps)])
        
        c=C*timestep/2. #This is so we don't need to multiply by the timestep many times
        d=D*timestep/2. #The half is because we do N(t/2) L(t) N(t/2),
        
        k1 = pyfftw.empty_aligned(xSteps, dtype='complex128')#These arrays are here so I don't need to reallocate memory to save temporary files
        k2 = pyfftw.empty_aligned(xSteps, dtype='complex128')
        k3 = pyfftw.empty_aligned(xSteps, dtype='complex128')
        k4 = pyfftw.empty_aligned(xSteps, dtype='complex128')
        ksum = pyfftw.empty_aligned(xSteps, dtype='complex128')
        absol = pyfftw.empty_aligned(xSteps, dtype='complex128')
        cterm = pyfftw.empty_aligned(xSteps, dtype='complex128')
        dterm = pyfftw.empty_aligned(xSteps, dtype='complex128')
        yield list(current_state)
        while True:
                #np.multiply(nonlinear(c,d,current_state,k1,k2,k3,k4,absol,cterm,dterm),pm,current_state)
                nonlinear(c,d,current_state,k1,k2,k3,k4,ksum,absol,cterm,dterm)
                np.multiply(current_state,pm,current_state)
                fft_object()
                np.multiply(fourier_state,LinList,fourier_state)
                ifft_object()
                np.multiply(current_state,pm,current_state)
                
                #current_state[:] = nonlinear(c,d,current_state,k1,k2,k3,k4,absol,cterm,dterm)
                nonlinear(c,d,current_state,k1,k2,k3,k4,ksum,absol,cterm,dterm)
                yield list(current_state)

def alltime(timestep,numtimesteps,A,B,C,D,RealLength,oldstate):
    gen = newgenerator(timestep,A,B,C,D,RealLength,oldstate)
    return [gen.next() for i in range(int(numtimesteps))]





#Put in a single value and get the evolution from the nonlinear part.
if 0: #this is to test if the nonlinear part is working
        def testRK(timestep,numtimesteps,C,D,oldstate):
                oldstate = [oldstate,0,0,0]
                allsteps = oldstate
                newstep = oldstate
                for i in range(int(numtimesteps)):
                        newstep = nonlinear(timestep,C,D,newstep)
                        allsteps = np.vstack((allsteps,newstep))
                return allsteps
        c=0.1+0.4*1j
        d=-0.1+0.1*1j
        initial_value = 1.
        finaltime = 1.
        
        timestep = 0.1

        allsteps = testRK(timestep,1.*finaltime/timestep,c,d,initial_value)[0:,0]#The last bit selects the first collumn. Only the first collumn contains interesting info, but all of it is needed to generate the output.
        print allsteps[-1]
        import matplotlib.pyplot as plt

        timearr = np.arange(0,finaltime+timestep,timestep)
        print np.shape(timearr)
        #print allsteps
        plt.plot(timearr, np.real(allsteps))
        plt.show()


if 0: #this is to test if the linear part is working
        #Make sure you run the mathematica code before you run this code.
        def testLin(timestep,numtimesteps,A,B,RealLength,oldstate):
            allsteps = oldstate
            newstep = oldstate
            for i in range(int(numtimesteps)):
                newstep = linear(timestep,A,B,RealLength,newstep)
                allsteps = np.vstack((allsteps,newstep))
            return allsteps
        
        a=3.+0.5*1j
        b=0.5-1j

        RealLength = 2*np.pi
        xstep = 0.001
        xpos = np.arange(0,RealLength,xstep)
        
        def initPsi(x):
                return np.sin(np.pi*np.cos(x))
        
        initial_state = [initPsi(x) for x in xpos]
        finaltime = 10.
        timestep = 0.01

        allsteps = testLin(timestep,1.*finaltime/timestep,a,b,RealLength, initial_state)
        finalState = allsteps[-1]

        import matplotlib.pyplot as plt
        if 1:               
                importdata = np.genfromtxt("testlinear.csv", delimiter = ',')
                mathlin = [i[0]+1j*i[1] for i in importdata]

                

                maxval = max(abs(finalState))
                percentError = [100*abs(P-M)/maxval for P,M in zip(finalState,mathlin)]
                print "Max percent error = " + str(max(percentError))+ "%"
                plt.plot(xpos, percentError)
                plt.show()
        
        if 1:
                plt.plot(xpos, np.real(finalState),'b-')
                plt.plot(xpos, np.real(mathlin),'g-')
                plt.show()
