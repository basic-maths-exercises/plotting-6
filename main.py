import matplotlib.pyplot as plt
import numpy as np

xvals = np.zeros(1000)
for i in range(1000) : xvals[i] = -np.pi + i*2*np.pi/999.

yvals = np.zeros(1000)
for i in range(1000) : yvals[i] = np.sin( xvals[i] )

plt.plot( xvals, yvals, 'k-' )
plt.savefig( "sine.png" )
