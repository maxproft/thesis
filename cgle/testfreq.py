import numpy as np
import bulk_run as b



#a = [np.sin(2.*np.pi*t*12) for t in np.linspace(0,0.5,2000)]
a = [12 for t in np.linspace(0,0.5,2000)]

freq = b.TimeFreq(a,0.5)
print(freq)
pred = [np.sin(2*np.pi*freq*t) for t in np.linspace(0,0.5,2000)]


import matplotlib.pyplot as plt

plt.plot(pred, 'r-')
plt.plot(a,'b.')

plt.show()
