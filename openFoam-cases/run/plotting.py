##########################################################################################################
# LIBRARY IMPORTING
##########################################################################################################

import matplotlib
#This is required to 'plot' inside the CLI
matplotlib.use('AGG')

import numpy as np
import matplotlib.pyplot as plt
import os
from parse import *
import sys

##########################################################################################################
# INPUT PARAMETER DEFINITION
##########################################################################################################

#Values taken from the calling in os.system()
route = sys.argv[1]
file = sys.argv[2]

#Examples lines to parse the values (2 are taken from this solver and turbulence model)
exampleLine1 = "Time = {}\n\
\n\
smoothSolver:  Solving for Ux, Initial residual = {}, Final residual = {}, No Iterations {}\n\
smoothSolver:  Solving for Uy, Initial residual = {}, Final residual = {}, No Iterations {}\n\
GAMG:  Solving for p, Initial residual = {}, Final residual = {}, No Iterations {}\n\
time step continuity errors : sum local = {}, global = {}, cumulative = {}\n\
smoothSolver:  Solving for epsilon, Initial residual = {}, Final residual = {}, No Iterations {}\n\
smoothSolver:  Solving for k, Initial residual = {}, Final residual = {}, No Iterations {}\n\
ExecutionTime = {} s  ClockTime = {} s\n\
\n\
forces forces write:\n\
    sum of forces:\n\
        pressure : ({} {} {})\n\
        viscous  : ({} {} {})\n\
        porous   : ({} {} {})\n\
    sum of moments:\n\
        pressure : ({} {} {})\n\
        viscous  : ({} {} {})\n\
        porous   : ({} {} {})\n\
\n"

exampleLine2 = "Time = {}\n\
\n\
smoothSolver:  Solving for Ux, Initial residual = {}, Final residual = {}, No Iterations {}\n\
smoothSolver:  Solving for Uy, Initial residual = {}, Final residual = {}, No Iterations {}\n\
GAMG:  Solving for p, Initial residual = {}, Final residual = {}, No Iterations {}\n\
time step continuity errors : sum local = {}, global = {}, cumulative = {}\n\
smoothSolver:  Solving for epsilon, Initial residual = {}, Final residual = {}, No Iterations {}\n\
bounding epsilon, min: {} max: {} average: {}\n\
smoothSolver:  Solving for k, Initial residual = {}, Final residual = {}, No Iterations {}\n\
ExecutionTime = {} s  ClockTime = {} s\n\
\n\
forces forces write:\n\
    sum of forces:\n\
        pressure : ({} {} {})\n\
        viscous  : ({} {} {})\n\
        porous   : ({} {} {})\n\
    sum of moments:\n\
        pressure : ({} {} {})\n\
        viscous  : ({} {} {})\n\
        porous   : ({} {} {})\n\
\n"

#Given that there are two example lines, some corrections are needed when storing data
exL12 = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41],
         [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]]

#Parameters to optimize and make plotting automatic
elementsPlot1 = [1,4,7,13,19]
confPlot1 = ['r','g','y','b','orange']
legendPlot1 = [r'$U_x$',r'$U_y$',r'$\varepsilon$',r'$k$',r'$p$']

elementsPlot2 = [11,12]
confPlot2 = ['g','r']
legendPlot2 = ['Global','Cumulative']

#As it is a 2D case, z components and porous stuff will not be considered
elementsPlot3 = [24,25,27,28,33,34,36,37]
confPlot3 = ['r','b','g','k','r','b','g','k']
legendPlot3 = [r'Pressure $F_x$',r'Pressure $F_y$',r'Viscous $F_x$',r'Viscous $F_y$',r'Pressure $M_x$',r'Pressure $M_y$',r'Viscous $M_x$',r'Viscous $M_y$']

##########################################################################################################
# MAIN FUNCTION
##########################################################################################################

#Read the file specified in the route and store it in "lines"
lines = []
with open (route + file, 'rt') as in_file:  
    for line in in_file: 
        lines.append(line) #Appends current line into lines

#The number of iterations will be the number that "Time =" occures divided by two ("Time = " and "ExecutionTime = ")
iterNo = int(len([s for s in lines if "Time = " in s])/2)

#Here exampleLine2 has more values to parse than exampleLine1, taking the size of the matrix from it
values = np.zeros((iterNo, exampleLine2.count('{}'))) 

#Iterate along the number of iterations
for i in range(1,iterNo):
	#exampleLine1
    if lines.index('Time = %i\n' %(i+1))-lines.index('Time = %i\n' %(i)) == exampleLine1.count('\n'): #If the lines between time i and time i+1 is the same as the \n in exampleLine1
        for j in range(exampleLine1.count('{}')): #For each {} in the exampleLine1 (i.e. a value to parse)
            values[i,exL12[0][j]] = float(parse(exampleLine1, ''.join(lines[lines.index('Time = %i\n' %(i)):lines.index('Time = %i\n' %(i+1))])).fixed[exL12[1][j]]) #Get that value
	#exampleLine2 (the same as above)
    elif lines.index('Time = %i\n' %(i+1))-lines.index('Time = %i\n' %(i)) == exampleLine2.count('\n'):
        for j in range(exampleLine2.count('{}')):
            values[i,j] = float(parse(exampleLine2, ''.join(lines[lines.index('Time = %i\n' %(i)):lines.index('Time = %i\n' %(i+1))])).fixed[j])
            
#Residuals plotting
fig, ax = plt.subplots(figsize=(16,8), dpi=100)
for i in range(len(elementsPlot1)):
    ax.semilogy(values[values[:,0] != 0,0],values[values[:,0] != 0,elementsPlot1[i]],c=confPlot1[i],label=legendPlot1[i])
ax.set_xlim(0,iterNo)
ax.set_ylim(None, 1)
ax.set_title('Residuals',fontsize=16)
ax.set_xlabel('Iteration',fontsize=12)
ax.set_ylabel('Initial residual',fontsize=12)
ax.legend()
ax.grid()
plt.savefig(route + 'residuals.png', bbox_inches = 'tight')
plt.close(fig)            

#Continuity plotting
fig, ax = plt.subplots(figsize=(16,8), dpi=100)
for i in range(len(elementsPlot2)):
    ax.plot(values[values[:,0] != 0,0],values[values[:,0] != 0,elementsPlot2[i]],c=confPlot2[i],label=legendPlot2[i])
ax.set_xlim(0,iterNo)
ax.set_title('Continuity',fontsize=16)
ax.set_xlabel('Iteration',fontsize=12)
ax.legend()
ax.grid()
plt.savefig(route + 'continuity.png', bbox_inches = 'tight')
plt.close(fig)

#Forces plotting
fig, (ax1, ax2) = plt.subplots(2, figsize=(10,10), dpi=100,  sharex=True)
for i in range(int(len(elementsPlot3)/2)):
    ax1.plot(values[values[:,0] != 0,0],values[values[:,0] != 0,elementsPlot3[i]],confPlot3[i],label=legendPlot3[i])
for i in range(int(len(elementsPlot3)/2),len(elementsPlot3)):
    ax2.plot(values[values[:,0] != 0,0],values[values[:,0] != 0,elementsPlot3[i]],confPlot3[i],label=legendPlot3[i])
ax1.set_xlim(0,iterNo)
ax1.set_title('Forces',fontsize=16)
ax1.set_xlabel('Iteration',fontsize=12)
ax1.set_ylabel('Force',fontsize=12)
ax1.legend()
ax1.grid()
ax2.set_title('Momentum',fontsize=16)
ax2.set_xlabel('Iteration',fontsize=12)
ax2.set_ylabel('Momentum',fontsize=12)
ax2.legend()
ax2.grid()
plt.savefig(route + 'forces.png', bbox_inches = 'tight')
plt.close(fig)
