import numpy as np
def nonlinde(C,D,oldstate):
        return np.array([C*x*abs(x)**2+D*x*abs(x)**4 for x in oldstate])

def nonlinear(timestep,C,D,oldstate):
    oldstate=np.array(oldstate)
    k1=nonlinde(C,D,oldstate)
    k2=nonlinde(C,D,oldstate+k1*timestep/2.)
    k3=nonlinde(C,D,oldstate+k2*timestep/2.)
    k4=nonlinde(C,D,oldstate+k3*timestep)

    return oldstate+(k1+2*k2+2*k3+k4)*timestep/6.

def linear(timestep,A,B,RealLength,oldstate):
    
    fourier = np.fft.fft([item * np.exp(1j*3.14159265*n) for n,item in enumerate(oldstate)])
    temp = [np.exp((A-B*(3.14159265*(2*m-len(oldstate))/RealLength)**2)*timestep)*item for m,item in enumerate(fourier)]
    invfft = np.fft.ifft(temp)
    return [item*np.exp(-1j*3.14159265*n) for n,item in enumerate(invfft)]

def oldlinear(timestep,A,B,RealLength,oldstate):
    print("WHY AM I IN OLDLINEAR?")
    power = -B*timestep*4.*3.14159265359**2/RealLength**2
    fourier = np.fft.fft(oldstate)
    temp = [np.exp(power*k**2+A*timestep)*item for k,item in enumerate(fourier)]
    return np.fft.ifft(temp)

def OLDFUNCTIONonestep(timestep,A,B,C,D,RealLength,oldstate):
        print("WHY AM I IN THE OLD FUNCTION??")
        power = -B*timestep*4.*3.14159265359**2/RealLength**2
        nonlin = nonlinear(timestep,C,D,oldstate)
        fourier = np.fft.fft(nonlin)
        temp = [np.exp(power*k**2+A*timestep)*item for k,item in enumerate(fourier)]
        return np.fft.ifft(temp)

def onestep(timestep,A,B,C,D,RealLength,oldstate):
        nonlinEvolution = nonlinear(timestep/2.,C,D,oldstate)
        linEvolution = linear(timestep,A,B,RealLength,nonlinEvolution)
        secondNonLinEvolution = nonlinear(timestep/2.,C,D,linEvolution)
        return secondNonLinEvolution
    
def alltime(timestep,numtimesteps,A,B,C,D,RealLength,oldstate):
    allsteps = oldstate
    newstep = oldstate
    for i in range(int(numtimesteps)-1):
        newstep = onestep(timestep,A,B,C,D,RealLength,newstep)
        allsteps = np.vstack((allsteps,newstep))
    return allsteps











#Put in a single value and get the evolution from the nonlinear part.
def testRK(timestep,numtimesteps,C,D,oldstate):
    oldstate = [oldstate,0,0,0]
    allsteps = oldstate
    newstep = oldstate
    for i in range(int(numtimesteps)):
        newstep = nonlinear(timestep,C,D,newstep)
        allsteps = np.vstack((allsteps,newstep))
    return allsteps

if 0: #this is to test if the nonlinear part is working
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












def testLin(timestep,numtimesteps,A,B,RealLength,oldstate):
    allsteps = oldstate
    newstep = oldstate
    for i in range(int(numtimesteps)):
        newstep = linear(timestep,A,B,RealLength,newstep)
        allsteps = np.vstack((allsteps,newstep))
    return allsteps

if 0: #this is to test if the linear part is working
        #Make sure you run the mathematica code before you run this code.
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



