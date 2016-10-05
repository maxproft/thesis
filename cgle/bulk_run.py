#!/usr/bin/python
#sys inputs are [path, subfolder, cpuID]
import numpy as np
from PIL import Image
import pythonCGLE as cgle
import os,sys
import pickle



########   Test if a list is not a soliton, has Nan, etc.    ##################
def periodicDist(x,mu,L):
        if x<mu-L*0.5:
                return abs(L-mu+x)
        elif x>mu+L*0.5:
            return abs(mu+L-x)
        else:
            return abs(mu-x)

def baddata(state):
        absol = np.abs(state)
        maximum = np.max(absol)
        total = np.sum(absol)

        
        if np.sum(np.isnan(absol))>0:
                return False
        elif maximum>10**5:
                return False
        elif total<1:
                return False
        
        L=len(absol)
        xlist = range(L)
        probdist = [height/total for x,height in zip(xlist,absol)]
        average = np.sum([x*p for x,p in zip(xlist,probdist)])
        nearmean = np.sum([h for h,x in zip(absol,xlist) if periodicDist(x,average,L)<L/4])
        if nearmean/total<0.65:
                return False
        else:
                return True

def std(data,xlength):
        prob = np.abs(data)/np.sum(np.abs(data))
        L=len(data)
        xlist = range(L)
        mean = np.sum([x*p for x,p in zip(xlist,prob)])
        std = np.sqrt(np.sum(  [p*periodicDist(x,mean,L)**2 for x,p in zip(xlist,prob)]))
        return std*xlength/L



########## Functions to make and save the data ###########

def BWImage(small_intensity,pathToPNG):
    def normalisedata(I):
        I = np.array(I)
        return (((I.max()-I) / (I.max() - I.min())) * 255.9).astype(np.uint8)
    img = Image.fromarray(np.flipud(normalisedata(small_intensity)))
    img.save(pathToPNG)

def SaveAllData(intensity,pathToAllCSV):
    np.savetxt(pathToAllCSV, np.array(intensity).view(float), delimiter=",")

def MakeData(inlist):
    uniqueId = inlist[0]
    timestep = inlist[1]
    numtimesteps = inlist[2]
    tpixels = inlist[3]
    A=inlist[4]
    B=inlist[5]+1j*0.5*inlist[6]
    C=inlist[7]+1j
    D=inlist[8]+1j*inlist[9]
    RealLength=inlist[10]
    xpixels=inlist[11]
    pathToSubfolder = inlist[12]
    pathToCSV = pathToSubfolder+str(uniqueId)+'.csv'
    pathToPNG = pathToSubfolder+str(uniqueId)+'.png'
    pathToAllCSV = pathToSubfolder+str(uniqueId)+'_AllData.csv'
    pathToExtra = pathToSubfolder+str(uniqueId)+'_extra.csv'
    oldstate = inlist[13]
    
    outarr = cgle.alltime(timestep,numtimesteps,tpixels,A,B,C,D,RealLength,xpixels,pathToCSV,oldstate)
    if len(outarr)!=0:
      if baddata(outarr[-1]):
        absol = np.abs(outarr)
        
        i,j = np.unravel_index(absol.argmax(), absol.shape)
        maxim = absol[i,j]
        minim = np.min(absol[:,j])
        HeightDiff = maxim-minim
        
        q = np.sum(absol*absol,axis=1)*RealLength/len(absol[0])
        qDiff = max(q)-min(q)

        stdlist = [std(data) for data in outarr]
        maxstd = max(stdlist)
        minstd = min(stdlist)
        stdDiff = maxstd-minstd
        
        np.savetxt(pathToExtra, np.array([HeightDiff,qDiff,maxstd,stdDiff]),delimiter=",")
        
        
        BWImage(np.abs(outarr),pathToPNG)
        
    #SaveAllData(outarr,pathToAllCSV) This uses ~1000 times more space on the harddrive than anything else.

if __name__=='__main__':
    sysIn = sys.argv
    if len(sysIn)<3:
        subfolder = 'bulk'
        cpuId=0
    else:
        subfolder = sysIn[1]
        cpuId = sysIn[2]
    
    currentfolder = os.getcwd()
    pathToSubfolder = currentfolder+'/'+subfolder+'/'

    file = open(pathToSubfolder+'cpu'+str(cpuId)+'.p','rb')
    allparams= pickle.load(file)
    file.close()
    for i in allparams:
            MakeData(i)
