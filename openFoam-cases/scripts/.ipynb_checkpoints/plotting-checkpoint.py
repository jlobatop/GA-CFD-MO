import numpy as np
import matplotlib.pyplot as plt
import os
from parse import *

lines = []
with open ('g0e0.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    for line in in_file: # Store each line in a string variable "line"
        lines.append(line) # prints that line

iterNo = int(len([s for s in lines if "Time = " in s])/2)

exampleLine1 = "Time = {}\n\
\n\
smoothSolver:  Solving for Ux, Initial residual = {}, Final residual = {}, No Iterations {}\n\
smoothSolver:  Solving for Uy, Initial residual = {}, Final residual = {}, No Iterations {}\n\
GAMG:  Solving for p, Initial residual = {}, Final residual = {}, No Iterations {}\n\
time step continuity errors : sum local = {}, global = {}, cumulative = {}\n\
smoothSolver:  Solving for epsilon, Initial residual = {}, Final residual = {}, No Iterations {}\n\
smoothSolver:  Solving for k, Initial residual = {}, Final residual = {}, No Iterations {}\n\
ExecutionTime = {} s  ClockTime = {} s\n\
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
\n"

exL12 = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,20,21,22,23],
         [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]

elementsPlot1 = [1,4,7,13,19]
confPlot1 = ['r','g','y','b','orange']
legendPlot1 = [r'$U_x$',r'$U_y$',r'$\varepsilon$',r'$k$',r'$p$']

elementsPlot2 = [11,12]
confPlot2 = ['g','r']
legendPlot2 = ['Global','Cumulative']

#Here exampleLine2 has more values to parse than exampleLine1
values = np.zeros((iterNo, exampleLine2.count('{}'))) 

for i in range(1,iterNo):
    if lines.index('Time = %i\n' %(i+1))-lines.index('Time = %i\n' %(i)) == exampleLine1.count('\n'): #configure for each exampleLine
        for j in range(len(exL12[0])):
            values[i,exL12[0][j]] = float(parse(exampleLine1, ''.join(lines[lines.index('Time = %i\n' %(i)):lines.index('Time = %i\n' %(i+1))])).fixed[exL12[1][j]])
    elif lines.index('Time = %i\n' %(i+1))-lines.index('Time = %i\n' %(i)) == exampleLine2.count('\n'):
        for j in range(exampleLine2.count('{}')):
            values[i,j] = float(parse(exampleLine2, ''.join(lines[lines.index('Time = %i\n' %(i)):lines.index('Time = %i\n' %(i+1))])).fixed[j])
            
print('llega aqui')
            
fig, ax = plt.subplots(figsize=(16,8), dpi=100)
for i in range(len(elementsPlot2)):
    ax.plot(values[values[:,0] != 0,0],values[values[:,0] != 0,elementsPlot2[i]],c=confPlot2[i],label=legendPlot2[i])
ax.set_xlim(0,iterNo)
ax.set_title('Continuity',fontsize=16)
ax.set_xlabel('Iteration',fontsize=12)
ax.legend()
ax.grid()
plt.savefig('continuity.png', bbox_inches = 'tight')
plt.close(fig)

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
plt.savefig('residuals.png', bbox_inches = 'tight')
plt.close(fig)