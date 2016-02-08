import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def plot(intensity, title="", name='a'):
    plt.close()
    plt.cla()
    plt.clf()
    #fig = matplotlib.figure.Figure
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    cmap = cm.get_cmap('hot_r')
    cs = plt.pcolor(intensity, cmap = cmap)
    cb = plt.colorbar(cs, orientation='vertical')
    plt.title(title)
    plt.savefig(g.solve['currentfolder']+'/'+g.solve['subfolder'] + '/' + str(name)+".png")
#    plt.show()
    #plt.close()


def make1D():
    global psi,savelist
    title = "A="+str(g.solve['A']) +"  B="+ str(g.solve['B']) + "  C="+ str(g.solve['C']) + "  D="+ str(g.solve['D'])
    size = int(float(g.solve['xtotal'])/float(g.solve['xstep']))
    psi = np.array([(np.random.rand()-0.5)*float(g.solve['randamp'])+1j*(np.random.rand()-0.5)*float(g.solve['randamp']) for y in range(size)])
    #psi = np.array([ float(g.solve['randamp'])*np.sin(y*size/(5*6.28))**2+1j*float(g.solve['randamp'])*np.cos(y*size/(5*6.28))**2 for y in range(size)])
    
    numframes = int(float(g.solve['ttotal'])/float(g.solve['tstep']))
    savelist = (np.array([int(x) for x in np.arange(0,numframes, numframes/(float(g.solve['giflen']) ))])+numframes/(float(g.solve['giflen'])))[3:]
    #I got rid of some of the early numbers, so that we have removed a lot of the noise
    
    def newpsi(N):
        global psi, savelist
        t=N*float(g.solve['tstep'])
        psiplus = np.append(psi[1:size],psi[size-1]) #these 1 lines make the edge pieces the same as the piece one inwards
        psiminus = np.insert(psi[0:size-1],0,psi[0])
        psi = float(g.solve['tstep'])*(g.solve['A']*psi + g.solve['B']*(psiplus+psiminus-2*psi)/(float(g.solve['xstep'])**2) + g.solve['C']*psi*np.abs(psi)**2 + g.solve['D']*psi*np.abs(psi)**4) + psi
        if N in savelist:
            if float(g.solve['absreal'])==0:
                return np.abs(psi)#/np.max(np.abs(psi))
            elif float(g.solve['absreal'])==1:
                return psi.real
        else:
            return None

    array = np.array([newpsi(N) for N in range(numframes+1)])
    array = np.array([x for x in array if x is not None])
    plot(array, title,name='1D Array')



def makegif():
    title = "A="+str(g.solve['A']) +"  B="+ str(g.solve['B']) + "  C="+ str(g.solve['C']) + "  D="+ str(g.solve['D'])
    size = int(float(g.solve['xtotal'])/float(g.solve['xstep']))
    psi = np.array([[(np.random.rand()-0.5)*float(g.solve['randamp'])+1j*(np.random.rand()-0.5)*float(g.solve['randamp']) for y in range(size)] for x in range(size)])
    numframes = int(float(g.solve['ttotal'])/float(g.solve['tstep']))
    savelist = (np.array([int(x) for x in np.arange(0,numframes, numframes/(float(g.solve['giflen']) ))])+numframes/(float(g.solve['giflen'])))[3:]
   #I got rid of some of the early numbers, so that we have removed a lot of the noise
    for N in range(numframes+1):
        t=N*float(g.solve['tstep'])
        psiplusx = np.hstack((psi[:,1:],np.transpose(psi[:,size-1][None])))
        psiplusy = np.vstack((psi[1:,:],psi[size-1,:]))
        psiminusx = np.hstack((np.transpose(psi[:,0][None]),psi[:,:size-1]))
        psiminusy = np.vstack((psi[0,:],psi[:size-1,:]))
        psi = float(g.solve['tstep'])*(g.solve['A']*psi + g.solve['B']*(psiplusx+psiplusy+psiminusx+psiminusy-4*psi)/(float(g.solve['xstep'])**2) + g.solve['C']*psi*np.abs(psi)**2 + g.solve['D']*psi*np.abs(psi)**4) + psi
        if N in savelist:
            if float(g.solve['absreal'])==0:
                intensity = np.abs(psi)#/np.max(np.abs(psi))
                plot(intensity, title=title, name=str(10**(int(np.log10(numframes+1))+1)+N))
            elif float(g.solve['absreal'])==1:
                intensity = psi.real
                plot(intensity, title=title, name=str(10**(int(np.log10(numframes+1))+1)+N))
    print "Making the GIF"
    os.system("convert -delay 10 -loop 0 "+g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"*.png "+g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"output.gif")

