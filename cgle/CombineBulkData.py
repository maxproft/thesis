import numpy as np
import os

folder = "AllDat"

allparams = np.loadtxt(folder+"/Params.csv", delimiter = ',')
#uniqueId(0),delta(1),beta(2),D(3),epsilon(4),mu(5),nu(6)


print(len(allparams))


def joinParamsAndOutput(folder, alldata):
    length = len(alldata)
    percent = int(length/100)
    for params in alldata:
        name = folder+'/'+str(int(params[0])).rjust(6,'0')+'_extra.csv'
        if int(params[0])%percent==0:
            print( str(int(params[0]/percent))+'% Completed')
        if os.path.isfile(name):
            outdat = np.loadtxt(name, delimiter=',')
            #dH(0),dQ(1),maxSTD(2),dSTD(3),freq(4)
            savedata = list(params[1:])
            savedata.append(outdat[1])
            yield savedata

joinedInfo = list(joinParamsAndOutput(folder, allparams))
print(str(len(joinedInfo)) + " Data Points")
np.savetxt("machLearnData.csv",np.array(joinedInfo), delimiter = ',')


