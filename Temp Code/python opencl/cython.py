import matplotlib.pyplot as plt
import numpy as np
import multiprocessing
import sys
length=50
mylist=[[x,2*x,3*x] for x in range(length)]

def myfunction(i,mylist=mylist):
    def longtime(): #This code adds about half a second for each calculation.
        a=np.array([5.00056515005865*(np.random.rand()+np.random.rand()+np.random.rand()+np.random.rand())+7.23513542*(np.random.rand()+np.random.rand()+np.random.rand()+np.random.rand()) for x in range(1000000)])
        a=a*a
        a=(a+a+3*a+1.24535743215*a)**1.735564
        a=1.5131435442*a*(3.16542354*a+1.453143*a)
    if i==5: #This is to test whether or not it will start another process or wait for it to finish.
        print( 'start')
        [longtime() for x in range(10)]
        print( 'stop')
    else:
        longtime()
    print( mylist[i])
    return i

def looping(i):
    pool =multiprocessing.Pool() #creates a pool of process, controls worksers
    result = pool.map(myfunction,range(i))
    pool.close() #we are not adding any more processes
    pool.join() #tell it to wait until all threads are done before going on
    sys.stdout.flush()
    return result



output = looping(length)
print( output)


