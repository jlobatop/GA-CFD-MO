import matplotlib
#This is required to 'plot' inside the CLI
matplotlib.use('AGG')

import numpy as np
import matplotlib.pyplot as plt
import sys

# Get the inputs from the terminal line
# Generation 
gen = int(sys.argv[1])
# Individual 
ind = int(sys.argv[2])
# Amplitude of the sine wave
amp = float(sys.argv[3])
# Frequency of the sine wave
freq = float(sys.argv[4])
# Number of elements in the file 
N = int(sys.argv[5])

# Create a file with the the AFC values
time = np.linspace(0,110,N)
vel = amp*np.sin(freq*time)

# Save velocity matrix
with open('./gen%i/ind%i/0/AFCvalues' %(gen, ind), 'w') as file:
    file.write('(\n')
    # Initial velocity of the AFC
    file.write('    (0.0 (0.0 0.0 0.0))\n')
    for i in range(N):
        file.write('    (%3.5f (%2.5f 0.0 0.0))\n' %(time[i]+40, vel[i]))
    file.write(')')    
    
# Save a figure with the selected AFC
fig, (ax1) = plt.subplots(1, figsize=(15,10))
ax1.plot(time+40, vel, 'b', linewidth = 2, label='AFC velocity inlet')
ax1.plot([0,40],[0,0], 'b', linewidth = 2)
ax1.set_xlim([0,150])
ax1.set_ylim([-2.5,2.5])
ax1.set_title('Active Flow Control',fontsize=16)
ax1.set_xlabel('Velocity inlet (m/s)',fontsize=12)
ax1.set_ylabel('Time (s)',fontsize=12)
ax1.legend()
plt.savefig('./gen%i/ind%i/0/AFCg%ii%i.png' %(gen, ind, gen, ind), bbox_inches = 'tight', dpi=100)