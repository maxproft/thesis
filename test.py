import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

numframes = 100000
numsave = 100
subfolder = 'pulse'



rootfolder = os.getcwd()
if not os.path.exists(rootfolder+'/'+subfolder):#making the subfolder, if it doesn't exist
    os.makedirs(rootfolder+'/'+subfolder)





#np.seterr(divide='ignore', invalid='ignore')



beta = 0.08
delta = -0.1
epsilon = 0.66
mu = -0.1
nu = -0.1
D = 1

title = "beta="+str(beta) +"delta="+ str(delta) + "epsilon="+ str(epsilon) + "mu="+ str(mu) + "nu="+ str(nu) + "D="+str( D)


#dimensions of the box
dimension = 50
#number of pixels along each side
size = 50


Tstep = 0.001 #time between frames





NORMAL = delta
XX = beta+1j*D/2.
FOUR = mu+1j*nu
TWO = epsilon+1j


Xstep = dimension/float(size) #distance to neighbouring squares


psi = np.array([[np.random.rand()*10-5+np.random.rand()*10j-5j for y in range(size)] for x in range(size)])


def plot(intensity, name='0',subfolder=subfolder):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    cmap = cm.get_cmap('hot_r')
    cs = plt.pcolor(intensity, cmap = cmap)
    cb = plt.colorbar(cs, orientation='vertical')
    plt.title(title)
    plt.savefig(rootfolder+'/'+subfolder + '/' + str(name)+".png")
#    plt.show()
    plt.close()




for t in range(numframes):
    psiplusx = np.hstack((psi[:,1:],np.transpose(psi[:,size-1][None])))
    psiplusy = np.vstack((psi[1:,:],psi[size-1,:]))
    psiminusx = np.hstack((np.transpose(psi[:,0][None]),psi[:,:size-1]))
    psiminusy = np.vstack((psi[0,:],psi[:size-1,:]))
    psi = Tstep*(NORMAL*psi + XX*(psiplusx+psiplusy+psiminusx+psiminusy-4*psi)/(Xstep**2) + TWO*psi*np.abs(psi)**2 + FOUR*psi*np.abs(psi)**4) + psi
    if t%int(numframes/numsave)==1:
        print str(int(t*100/numframes))+'%'
        #intensity = np.abs(psi)#/np.max(np.abs(psi))
        intensity = psi.real
        plot(intensity, name=str(10**(int(np.log10(numframes))+1)+t))

intensity = np.abs(psi)#/np.max(np.abs(psi))
plot(intensity, name=str(10**(int(np.log10(numframes))+1)+t))

print "sleeping"

import time
time.sleep(10) # delays for 5 seconds

print "Making the GIF"
os.system("convert -delay 10 -loop 0 "+rootfolder+'/'+subfolder+'/'+"*.png "+rootfolder+'/'+subfolder+'/'+"output.gif")





