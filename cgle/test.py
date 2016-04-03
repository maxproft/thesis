import FortranCGLE as cgle
import numpy as np




mylist=np.complex64([(x+x*1j)/100 for x in range(10000)])
comp1=(1+3*1j)*0.001
comp2=(6+7*1j)*0.001
comp3=(4+5*1j)*0.001
comp4=(3+6*1j)*0.001
delta = 0.002
#print cgle.arr2arr(mylist,2)
#print cgle.circlearea(3.5)
nextstep = cgle.nextstep(delta,comp1,comp2,comp3,comp4,mylist,100)


print nextstep
