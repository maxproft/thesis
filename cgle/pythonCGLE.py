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
    power = -B*timestep*4.*3.14159265359**2/RealLength**2
    fourier = np.fft.fft(oldstate)
    temp = [np.exp(power*k**2+A*timestep)*item for k,item in enumerate(fourier)]
    return np.fft.ifft(temp)

def OLDFUNCTIONonestep(timestep,A,B,C,D,RealLength,oldstate):
        print("WHY AM I IN THE ONESTEP FUNCTION??")
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


