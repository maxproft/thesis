import numpy as np
def nonlinear(timestep,C,D,oldstate):
    def nonlinde(C,D,oldstate):
        return np.array([C*x*abs(x)**2+D*x*abs(x)**4 for x in oldstate])
    oldstate=np.array(oldstate)
    k1=nonlinde(C,D,oldstate)
    k2=nonlinde(C,D,oldstate+k1*timestep/2.)
    k3=nonlinde(C,D,oldstate+k2*timestep/2.)
    k4=nonlinde(C,D,oldstate+k3*timestep)

    return oldstate+(k1+2*k2+2*k3+k4)*timestep/6.

def alltime(timestep,numtimesteps,A,B,C,D,RealLength,oldstate):
    
    def onestep(timestep,A,B,C,D,RealLength,oldstate):
        power = -B*timestep*4.*3.14159265359**2/RealLength**2
        nonlin = nonlinear(timestep,C,D,oldstate)
        fourier = np.fft.fft(nonlin)
        temp = [np.exp(power*k**2+A*timestep)*item for k,item in enumerate(fourier)]
        return np.fft.ifft(temp)
    temp = [onestep(timestep,A,B,C,D,RealLength,oldstate) for i in range(int(numtimesteps)-1)]
    return np.vstack((oldstate,temp))


