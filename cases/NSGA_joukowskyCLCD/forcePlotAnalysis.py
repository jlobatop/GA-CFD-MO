# Package importation
import matplotlib
#This is required to 'plot' inside the CLI
matplotlib.use('AGG')
import numpy as np
import matplotlib.pyplot as plt
from parse import *
import sys

################################################################################
#                                    INPUTS                                    # 
################################################################################
# Get the inputs from the terminal line
gen = int(sys.argv[1])
ind = int(sys.argv[2])

# Define the expected header of the forces.dat file
header = ["time",
          "pressureF_x","pressureF_y","pressureF_z",
          "viscousF_x","viscousF_y","viscousF_z",
          "porousF_x","porousF_y","porousF_z",
          "pressureM_x","pressureM_y","pressureM_z",
          "viscousM_x","viscousM_y","viscousM_z",
          "porousM_x","porousM_y","porousM_z"]

# Give a example line to parse
exampleLine = "{}\t(({} {} {}) ({} {} {}) ({} {} {})) (({} {} {}) ({} {} {}) ({} {} {}))\n"

# Read the file and store it in "lines"
lines = []
with open ('./gen%i/ind%i/postProcessing/forces/0/forces.dat' %(gen, ind), 'rt') as in_file:  
    for line in in_file: 
        lines.append(line) #Appends current line into lines
        
# forces matrix will have len(lines) rows and 19 columns:
# time-Fxp-Fyp-Fzp-Fxv-Fyv-Fzv-Fxp-Fyp-Fzp-Mxp-Myp-Mzp-Mxv-Myv-Mzv-Mxp-Myp-Mzp 
forces = np.zeros((len(lines), 19)) 

# Iterate along the number of rows (timesteps)
for i in range(len(lines)):
    # Check if there is ocurrences in the line
    if parse(exampleLine, lines[i]) != None:
        # If there are ocurrences, copy them into the array
        for j in range(19):
            forces[i,j] = float(parse(exampleLine, lines[i])[j])
            
# Remove the zeros in the matrix that may exist due to preallocation
forces = forces[forces[:,0] != 0]

################################################################################
#                                   PLOTTING                                   # 
################################################################################
# Fancy plot settings
plt.style.use('seaborn-deep')
plt.style.use('classic')
matplotlib.rcParams['axes.linewidth'] = 1.3
matplotlib.rcParams['lines.linewidth'] = 1.3
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r"\usepackage{amsmath}"]
matplotlib.rcParams.update({'font.size': 8})

# Figure definition
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(20,15))
fig.subplots_adjust(wspace=0.3, hspace=0.25)

# Upper left subplot
ax1.plot(forces[:,0],forces[:,1],'b',linewidth=3,label='Pressure Force X')
ax1.plot(forces[:,0],forces[:,2],'g',linewidth=3,label='Pressure Force Y')
ax1.set_ylim(-1*np.max(np.abs([forces[-1,1:3]])),2*np.max(np.abs([forces[-1,1:3]])))
ax1.set_xlabel(r'Iteration Number', fontsize=24)
ax1.set_ylabel(r'Force (N)', fontsize=24)
ax1.legend(loc='upper right', fontsize=20)
ax1.tick_params(labelsize=26)

# Upper right subplot
ax2.plot(forces[:,0],forces[:,4],'r',linewidth=3,label='Viscous Force X')
ax2.set_ylim(0,2*np.abs([forces[-1,4]]))
ax2.set_xlabel(r'Iteration Number', fontsize=24)
ax2.set_ylabel(r'Force (N)', fontsize=24)
ax2.legend(loc='upper right', fontsize=20)
ax2.tick_params(labelsize=26)

# Lower left subplot
ax3.plot(forces[:,0],forces[:,12],'m',linewidth=3,label='Pressure Moment Z')
ax3.set_ylim(-2*np.abs([forces[-1,12]]),2*np.abs([forces[-1,12]]))
ax3.set_xlabel(r'Iteration Number', fontsize=24)
ax3.set_ylabel(r'Moment (N m)', fontsize=24)
ax3.legend(loc='lower right', fontsize=20)
ax3.tick_params(labelsize=26)

# Lower right subplot
ax4.plot(forces[:,0],forces[:,15],'k',linewidth=3,label='Viscous Moment Z')
ax4.set_ylim(-2*np.abs([forces[-1,15]]),2*np.abs([forces[-1,15]]))
ax4.set_xlabel(r'Iteration Number', fontsize=24)
ax4.set_ylabel(r'Moment (N$\cdot$m)', fontsize=24)
ax4.legend(loc='upper right', fontsize=20)
ax4.tick_params(labelsize=26)

# General figure title
fig.suptitle('Generation %i Individual %i' %(gen, ind), fontsize=30)

# Figure saving
plt.savefig('./gen%i/data/CONg%ii%i.png' %(gen, gen, ind), bbox_inches='tight', dpi=100)

################################################################################
#                                FITNESS DATA                                  # 
################################################################################
np.savetxt('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind),
          np.array((forces[-1,1]+forces[-1,4],forces[-1,2]+forces[-1,5])))