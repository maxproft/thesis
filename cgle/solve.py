import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm




def TrialFunction(dist):
    if g.solve['trialfunction']=='0':
        return (np.random.rand()-0.5)*float(g.solve['par1'])+1j*(np.random.rand()-0.5)*float(g.solve['par1'])
    elif g.solve['trialfunction']=='1':#sech pulse
        return float(g.solve['par1'])*(np.cosh(dist/float(g.solve['par2']))**-1)*np.exp(1j*(float(g.solve['par4'])+float(g.solve['par5'])*dist+float(g.solve['par6'])*dist**2))
    elif g.solve['trialfunction']=='2':#Generalised Gaussian
        return float(g.solve['par1'])*np.exp(-dist**2/float(g.solve['par2'])**2-dist**4/(4*float(g.solve['par7'])*float(g.solve['par2'])**4)+1j*float(g.solve['par6'])*dist**2)

def iszero(x):
    if x==0:
        return 1
    else:
        return x

def toobig():
    if g.solve['One Error']==0:
        g.solve['One Error']=1
        print("Overflow Error")

def maxmin(x):
    if np.isnan(np.abs(x)):
        toobig()
        return 10**5+0*1j
    elif np.abs(x)>10**5:
        toobig()
        return 10**5+0*1j
    elif np.abs(x)<10**-5:
        return 10**-5+0*1j
    else:
        return x
vmaxmin=np.vectorize(maxmin)

def plot(intensity, title="", name='a'):
    if 0:
        plt.close()
        plt.cla()
        plt.clf()
        plt.plot(intensity[0])
        plt.plot(intensity[1])
        plt.plot(intensity[-1])
        plt.show()
    
    np.savetxt(g.solve['currentfolder']+'/'+g.solve['subfolder'] + '/' + str(name)+".csv", intensity, delimiter=",")

    plt.close()
    plt.cla()
    plt.clf()
    rows,cols = np.shape(intensity)
    if cols<rows:
        intensity = intensity[-cols:]
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
    g.solve['One Error']=0
    title = "A="+str(g.solve['A']) +"  B="+ str(g.solve['B']) + "  C="+ str(g.solve['C']) + "  D="+ str(g.solve['D'])
    size = int(float(g.solve['xtotal'])/float(g.solve['xstep']))
    if g.solve['trialfunction']=='3':
        psi = g.solve['psi']
    else:
        psi = np.array([ TrialFunction((y-size/2.)*float(g.solve['xstep'])-float(g.solve['par3'])) for y in range(size)])
    np.savetxt(g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"start.txt", psi.view(float))
    numframes = int(float(g.solve['ttotal'])/float(g.solve['tstep']))
    savelist = (np.array([int(x) for x in np.arange(0,numframes+numframes/(float(g.solve['tpixels'])), numframes/(float(g.solve['tpixels']) ))]))
    #pixelsavelist = (np.array([int(x) for x in np.arange(0,float(g.solve['xtotal'])/float(g.solve['xstep'])+float(g.solve['xtotal']/(float(g.solve['xpixels'])*float(g.solve['xstep']))),float(g.solve['xtotal']/(float(g.solve['xpixels'])*float(g.solve['xstep']))) )]))
    #I got rid of some of the early numbers, so that we have removed a lot of the noise

    def newpsi(N):
        global psi, savelist
        t=N*float(g.solve['tstep'])
        psiplus = np.append(psi[1:size],psi[size-1]) #these 1 lines make the edge pieces the same as the piece one inwards
        psiminus = np.insert(psi[0:size-1],0,psi[0])
        psi = float(g.solve['tstep'])*(g.solve['A']*psi + g.solve['B']*(psiplus+psiminus-2*psi)/(float(g.solve['xstep'])**2) + g.solve['C']*psi*np.abs(psi)**2 + g.solve['D']*psi*np.abs(psi)**4) + psi
        psi=vmaxmin(psi)
        if N in savelist:
            psiplot = psi[0::iszero(int(float(g.solve['xtotal'])/(float(g.solve['xpixels'])*float(g.solve['xstep']))))]
            if float(g.solve['absreal'])==0:
                return np.abs(psiplot)#/np.max(np.abs(psi))
            elif float(g.solve['absreal'])==1:
                return psiplot.real
        else:
            return None
    
    array = np.array([newpsi(N) for N in range(numframes+1)])
    np.savetxt(g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"end.txt", psi.view(float))
    array = np.array([x for x in array if x is not None])
    plot(array, title,name='1D Array')



def makegif():
    g.solve['One Error']=0
    title = "A="+str(g.solve['A']) +"  B="+ str(g.solve['B']) + "  C="+ str(g.solve['C']) + "  D="+ str(g.solve['D'])
    size = int(float(g.solve['xtotal'])/float(g.solve['xstep']))
    if g.solve['trialfunction']=='3':
        psi = g.solve['psi']
    else:
        psi = np.array([[ TrialFunction(((y-size/2.)**2+(x-size/2.)**2)**0.5*float(g.solve['xstep'])-float(g.solve['par3'])) for y in range(size)] for x in range(size)])
    np.savetxt(g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"start.txt", psi.view(float))
    numframes = int(float(g.solve['ttotal'])/float(g.solve['tstep']))
    savelist = (np.array([int(x) for x in np.arange(0,numframes+numframes/(float(g.solve['tpixels'])), numframes/(float(g.solve['tpixels']) ))]))
   #I got rid of some of the early numbers, so that we have removed a lot of the noise
    for N in range(numframes+1):
        t=N*float(g.solve['tstep'])
        psiplusx = np.hstack((psi[:,1:],np.transpose(psi[:,size-1][None])))
        psiplusy = np.vstack((psi[1:,:],psi[size-1,:]))
        psiminusx = np.hstack((np.transpose(psi[:,0][None]),psi[:,:size-1]))
        psiminusy = np.vstack((psi[0,:],psi[:size-1,:]))
        psi = float(g.solve['tstep'])*(g.solve['D']*psi*np.abs(psi)**4) + psi
        #psi = float(g.solve['tstep'])*(g.solve['A']*psi + g.solve['B']*(psiplusx+psiplusy+psiminusx+psiminusy-4*psi)/(float(g.solve['xstep'])**2) + g.solve['C']*psi*np.abs(psi)**2 + g.solve['D']*psi*np.abs(psi)**4) + psi
        psi=vmaxmin(psi)

        if N in savelist:
            psiplot = psi[0::iszero(int(float(g.solve['xtotal'])/(float(g.solve['xpixels'])*float(g.solve['xstep'])))),0::iszero(int(float(g.solve['xtotal'])/(float(g.solve['xpixels'])*float(g.solve['xstep']))))]
            if float(g.solve['absreal'])==0:
                intensity = np.abs(psiplot)#/np.max(np.abs(psi))
                plot(intensity, title=title, name=str(10**(int(np.log10(numframes+1))+1)+N))
            elif float(g.solve['absreal'])==1:
                intensity = psiplot.real
                plot(intensity, title=title, name=str(10**(int(np.log10(numframes+1))+1)+N))
    np.savetxt(g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"end.txt", psi.view(float))
    print("Making the GIF")
    os.system("convert -delay 10 -loop 0 "+g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"*.png "+g.solve['currentfolder']+'/'+g.solve['subfolder']+'/'+"output.gif")

