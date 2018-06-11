# Package importation
import numpy as np
import sys
import os

################################################################################
#                                    INPUTS                                    # 
################################################################################
# Get the inputs from the terminal line
gen = float(sys.argv[1])

################################################################################
#                                   MAIN BODY                                  # 
################################################################################
# Get the values of the search space 
x1 = np.genfromtxt('./gen%i/popA%i' %(gen, gen))
x2 = np.genfromtxt('./gen%i/popf%i' %(gen, gen))

# Get the number of individuals
N = len(x1)

# Loop over all individuals
for ind in range(N):
	# Get the lift, drag and area values for each individual
    sigmaX = np.genfromtxt('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind))[2] 
    sigmaY = np.genfromtxt('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind))[3] 
    # Save the values of the search space and the function value toghether in a file
    with open('./data/gen%i.txt' %gen, 'a') as file:
        file.write(",".join([str(x1[ind]),str(x2[ind]),str(sigmaX),str(sigmaY)]))
        file.write("\n")