#!/usr/bin/python
import numpy as np
import os,sys
import multiprocessing as mp
import pickle
#import numpy.random.uniform as uni
def params_for_multi(subfolder):

    currentfolder = os.getcwd()
    pathToSubfolder = currentfolder+'/'+subfolder+'/'
    #make subfolder
    if not os.path.exists(currentfolder+'/'+subfolder):#making the subfolder, if it doesn't exist
        os.makedirs(currentfolder+'/'+subfolder)


############## Making the parameters to test ###############

#The order is the following:
#uniqueId(0),timestep(1),numtimesteps(2),tpixels(3),delta(4),beta(5),D(6),epsilon(7),mu(8),nu(9),RealLength(10),xpixels(11),pathToSubfolder(12),oldstate(13)
    def IdGen():
        i=0
        while True:
            yield str(i).rjust(6,'0')
            i+=1

    identity = IdGen()
    timestep = 0.01
    numtimesteps = 5000.*0.5
    tpixels = 800
    if 1:
        deltaList =(-0.5,0.1)
        betaList = (0.,0.2)
        DList = (-1.5,1.5)
        epsilonList = (0.5,1.)
        muList = (-0.13,-0.07)
        nuList = (-0.05,-0.11)
    if 0:
        deltaList =(-0.1,-0.1) 
        betaList = (0.08,0.08)
        DList = (1,1)
        epsilonList = (0.6,0.7) 
        muList = (-0.1,-0.1)
        nuList = (-0.09,-0.05)
    RealLength = 40.
    xpixels = 800
    xres = 0.01
    oldstate = [2*np.exp(-x**2/9) for x in np.arange(-RealLength/2.,RealLength/2.,xres)]

    def uni(mytup):
        a,b = mytup
        return float(np.random.uniform(a,b))

    
    numsimulations = 8*10
    allparams = list([[next(identity), timestep,numtimesteps, tpixels,
                  uni(deltaList),uni(betaList),uni(DList),uni(epsilonList),uni(muList),uni(nuList),
                  RealLength,xpixels,pathToSubfolder,oldstate] for i in range(numsimulations)])
    #print(allparams)
             
    #allparams = list([[next(identity), timestep,numtimesteps, tpixels,delta,beta,D,epsilon,mu,nu,RealLength,xpixels,pathToSubfolder,oldstate]
             #for delta in deltaList   for beta in betaList   for D in DList   for epsilon in epsilonList   for mu in muList   for nu in nuList])

    


#This is saved in the following way:
#uniqueId(0),delta(1),beta(2),D(3),epsilon(4),mu(5),nu(6)
#print(paramsExport[10]) to get the info about file with identifier '10'
    def col(arr,n):
        return [[float(row[n])] for row in arr]
    paramsExport = np.hstack((col(allparams,0),col(allparams,4),col(allparams,5),col(allparams,6),col(allparams,7),col(allparams,8),col(allparams,9)))
    np.savetxt(pathToSubfolder + 'Params.csv', paramsExport, delimiter=",")


    cpu = mp.cpu_count()
    sublistsize = int(len(allparams)/cpu)+1

    for i in range(cpu):
        file = open(pathToSubfolder+'cpu'+str(i)+'.p','wb')
        pickle.dump(allparams[i*sublistsize:(i+1)*sublistsize],file)
        file.close()

    

if __name__ == '__main__':
    sysIn = sys.argv
    if len(sysIn)==1:
        params_for_multi('bulk')
    else:
        params_for_multi(str(sysIn[1]))





