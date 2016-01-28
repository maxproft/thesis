import numpy as np
import matplotlib.pyplot as plt
import os,sys,pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


beta = 0.08
delta = -0.1
epsilon = 0.66
mu = -0.1
nu = -0.1
D = 1


#dimensions of the box
dimension = 10
#number of pixels along each side
size = 100

Tstep = 0.0001 #time between frames





NORMAL = 1j*delta
XX = 1j*beta-D/2.
T = 1j
FOUR = 1j*mu-nu
TWO = 1j*epsilon-1


Xstep = dimension/float(size) #distance to neighbouring squares


psi = np.array([[x+1j*y for y in range(size)] for x in range(size)])


def plot(intensity):
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(intensity, cmap=plt.cm.get_cmap('hot_r'))
    plt.show()


for t in range(50):
    psiplusx = np.hstack((psi[:,1:],np.transpose(psi[:,size-1][None])))
    psiplusy = np.vstack((psi[1:,:],psi[size-1,:]))
    psiminusx = np.hstack((np.transpose(psi[:,0][None]),psi[:,:size-1]))
    psiminusy = np.vstack((psi[0,:],psi[:size-1,:]))
    psi = Tstep/T*(NORMAL*psi+XX*(psiplusx+psiplusy+psiminusx+psiminusy-4*psi)/Xstep**2+TWO*psi*np.abs(psi)**2 + FOUR*psi*np.abs(psi)**4)+psi
    if t%10==1:
        intensity = np.abs(psi)/np.max(np.abs(psi))
        plot(intensity)
