# Package importation
import numpy as np
import math
import random
import scipy.stats as stats
import optunity
from problemSetup import *

################################################################################
#                              FUNCTION DEFINITION                             # 
################################################################################
def initialization(N, randomInit, sobolInit, equalInit):
    """
    Initialization the population 
    
    INPUTS:
    N:                number of individuals (perfect square for equalInit)
    randomInit:       True for random initialization
    sobolInit:        True for Sobol sampling
    equalInit:        True for equally-spaced point distribution
    limits:           limits of the search domain: [x_low, x_high, y_low, y_high]
    (constrainedPts): function that returns a masked array for constrained points
    
    OUTPUTS:    
    initialPop:       numpy.ndarray with the initial N individuals

    This function computes the initial population for a two variable problem with 
    different sampling techniques: random initialization, Sobol sampling and 
    equally-spaced point distribution
    """

    # Check the flags to select the initialization method
    if np.sum([randomInit, sobolInit, equalInit]) > 1:
        raise RuntimeError('Incorrect initialization type selection')
    if np.sum([randomInit, sobolInit, equalInit]) == 0:
        raise RuntimeError('No initialization type selected')
    
    # Random initialization
    # Transpose is used to have the number of individuals in rows and coordinates in columns
    if randomInit:
        initialPop = np.array([x_low+np.random.rand(N)*(x_high-x_low),
                           y_low+np.random.rand(N)*(y_high-y_low)]).T
        
    # Sobol sampling
    if sobolInit:
        x1, x2 = zip(*optunity.solvers.Sobol.i4_sobol_generate(2, N, int(np.sqrt(N))))
        initialPop = np.vstack(((x_high - x_low) * np.array([x1]) + x_low,
                               (y_high - y_low) * np.array([x2]) + y_low)).T
        
    # Equally-spaced point distribution
    if equalInit:
        a, b = np.meshgrid(np.linspace(x_low,x_high,int(np.sqrt(N))), np.linspace(y_low,y_high,int(np.sqrt(N))))
        initialPop = np.vstack((np.reshape(a, len(a)**2),np.reshape(b, len(b)**2))).T
        
    # Constrained values will be replaced with a random numbers in its places
    while sum(constrainedPts(initialPop, const, constVal, compMode)) != 0:
        # The points where the constraints are not fulfilled ...
        boolMat = constrainedPts(initialPop, const, constVal, compMode)
        # ... are replaced with random numbers
        for i in np.argwhere(boolMat == True):
            initialPop[i] = np.array([x_low+np.random.rand(1)*(x_high-x_low),y_low+np.random.rand(1)*(y_high-y_low)]).T

    return initialPop

################################################################################
#                                   MAIN BODY                                  # 
################################################################################
# Let's initialize the population with 2N individuals
population = initialization(2*N, False, True, False)

# Save the population in the correspondant file
np.savetxt('./gen0/popx0', population[:,0], fmt='%.8f', delimiter=',')
np.savetxt('./gen0/popy0', population[:,1], fmt='%.8f', delimiter=',')