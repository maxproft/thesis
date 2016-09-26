#!/usr/bin/python
#sys inputs are [path, subfolder, cpuID]
import numpy as np
from PIL import Image
import pythonCGLE as cgle
import os,sys
import pickle


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
    oldstate = inlist[13]
    
    outarr = cgle.alltime(timestep,numtimesteps,tpixels,A,B,C,D,RealLength,xpixels,pathToCSV,oldstate)
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
