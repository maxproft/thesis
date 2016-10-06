import numpy as np
import bulk_run as b
import matplotlib.pyplot as plt


a = [(x-1.)**2 for x in np.linspace(0,2,100)]
a = [-(x-1.5)**2+2 for x in np.linspace(0,2,100)]
a = np.abs(a)
centre = np.argmax(a)
distlist = np.array([b.periodicDist(x,centre,len(a)) for x in range(len(a))])
c = b.std(a, 2., distlist)



plt.plot(a)
plt.show()
