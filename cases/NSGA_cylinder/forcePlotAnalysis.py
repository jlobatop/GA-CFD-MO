import matplotlib
#This is required to 'plot' inside the CLI
matplotlib.use('AGG')

import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import io
import sys

# Get values from the input
gen = int(sys.argv[1])
ind = int(sys.argv[2])

# Read the file efficientyly
s = open('./gen%i/ind%i/postProcessing/forces/0/forces.dat' %(gen, ind)).read().replace('(',' ').replace(')',' ').replace('\t',' ')
forces = np.genfromtxt(io.BytesIO(s.encode()))

# RMS function
def rms(x):
    return np.sqrt(np.mean(x**2))

# Plot a figure with forces evolution
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(20,15))

ax1.plot(forces[100:,0],forces[100:,1],'b',linewidth=2,label='Pressure Force X')
ax1.plot(forces[100:,0],forces[100:,2],'g',linewidth=2,label='Pressure Force Y')
ax1.set_xlabel('Time (s)', fontsize=16)
ax1.set_ylabel(r'Force ($N$)', fontsize=16)
ax1.legend(loc='lower left', fontsize=16)
ax1.tick_params(labelsize=14)

ax2.plot(forces[100:,0],forces[100:,4],'r',linewidth=2,label='Viscous Force X')
ax2.plot(forces[100:,0],forces[100:,5],'c',linewidth=2,label='Viscous Force Y')
ax2.set_xlabel('Time (s)', fontsize=16)
ax2.set_ylabel(r'Force ($N$)', fontsize=16)
ax2.legend(loc='upper right', fontsize=16)
ax2.tick_params(labelsize=14)

ax3.plot(forces[100:,0],forces[100:,10],'k',linewidth=2,label='Pressure Moment X')
ax3.set_xlabel('Time (s)', fontsize=16)
ax3.set_ylabel(r'Moment ($N\cdot m$)', fontsize=16)
ax3.legend(loc='lower left', fontsize=16)
ax3.tick_params(labelsize=14)

ax4.plot(forces[100:,0],forces[100:,12],'m',linewidth=2,label='Pressure Moment Z')
ax4.set_xlabel('Time (s)', fontsize=16)
ax4.set_ylabel(r'Moment ($N\cdot m$)', fontsize=16)
ax4.legend(loc='lower left', fontsize=16)
ax4.tick_params(labelsize=14)
plt.savefig('./gen%i/ind%i/VALg%ii%i.png' %(gen, ind, gen, ind), bbox_inches='tight', dpi=100)


# Get 
timestp40 = int(np.argwhere(forces[:,0]>40)[0])

matFX = np.invert(forces[timestp40:,1] > forces[-1,1])
logicFX = np.logical_xor(matFX[0:-2],matFX[1:-1])
if len(np.argwhere(logicFX))%2 == 1:
    fx = int(np.argwhere(logicFX)[1])
else:
    fx = int(np.argwhere(logicFX)[0])

matFY = np.invert(forces[timestp40:,2] > forces[-1,2])
logicFY = np.logical_xor(matFY[0:-2],matFY[1:-1])
if np.sum(logicFY) == 0:
	fy = timestp40
else:
	if len(np.argwhere(logicFY))%2 == 1:
	    fy = int(np.argwhere(logicFY)[1])
	else:
	    fy = int(np.argwhere(logicFY)[0])
    
    
fig, (ax1) = plt.subplots(1, figsize=(10,8))

ax1.plot(forces[timestp40+fx:,0],forces[timestp40+fx:,1]+forces[timestp40+fx:,4],'b',linewidth=2,label='Pressure Force X')
# ax1.plot(forces[timestp40+fx:,0],np.mean(forces[timestp40+fx:,1])*np.ones(len(forces[timestp40+fx:,0])),':b',linewidth=1)
ax1.plot(forces[timestp40+fy:,0],forces[timestp40+fy:,2]+forces[timestp40+fy:,5],'g',linewidth=2,label='Pressure Force Y')
# ax1.plot(forces[timestp40+fy:,0],np.mean(forces[timestp40+fy:,2])*np.ones(len(forces[timestp40+fy:,0])),':g',linewidth=1)
ax1.set_xlabel('Time (s)', fontsize=16)
ax1.set_ylabel(r'Force ($N$)', fontsize=16)
ax1.legend(loc='lower left', fontsize=16)
ax1.tick_params(labelsize=14)
ax1.set_ylim([-0.3,0.3])
ax1.set_xlim([0,150])
plt.savefig('./gen%i/data/OSCg%ii%i.png' %(gen, gen, ind), bbox_inches='tight', dpi=100)


np.savetxt('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind),
          np.array([np.mean(forces[timestp40+fx:,1]+forces[timestp40+fx:,4]),np.mean(forces[timestp40+fy:,2]+forces[timestp40+fy:,5]),
          			np.std(forces[timestp40+fx:,1]+forces[timestp40+fx:,4]),np.std(forces[timestp40+fy:,2]+forces[timestp40+fy:,5]),
                    rms(forces[timestp40+fx:,1]+forces[timestp40+fx:,4]),rms(forces[timestp40+fy:,2]+forces[timestp40+fy:,5])]))