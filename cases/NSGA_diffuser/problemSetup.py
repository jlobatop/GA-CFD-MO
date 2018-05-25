# Package importation
import numpy as np
import math
import random
import scipy.stats as stats
import optunity

################################################################################
#                                    INPUTS                                    # 
################################################################################
# Number of individuals per generation (it must be a 2^N number for parallel computing)
N = 32

# Defintion of the search spaces limits
x_low = 0.23583984
x_high = 2.5
y_low = 2.2906100426385296
y_high = 22.973531732579914
Lmax = 0.8
Lmin = 0.1

# Type of the constraints (including the limit constraints)
constVal = [x_high, x_low, y_high, y_low, Lmax, Lmin]
compMode = ['leq', 'geq', 'leq', 'geq', 'leq', 'geq']

################################################################################
#                                  FUNCTION                                    # 
################################################################################
def const(x,y,no):
    """Parameter space constraints for x and y values
    
    INPUTS:
    x:      first parameter search space component as numpy.ndarray
    y:      second parameter search space component as numpy.ndarray
    no:     number of the constraint that wants to be evaluated
    (although not an input, this function should be used with constVal and
    compMode lists that have the constraints values)
    
    OUTPUTS:
    array:  mutated individual as numpy.ndarray
    
    This function evaluates the constraints for the set of values in x and y in the
    desired function no-th. This follows Python notation where the first function is
    0, the second is 1,...
    """
    
    # Conditional for domain
    if no == 0:
        return x
    if no == 1:
        return x
    if no == 2:
        return y
    if no == 3:
        return y
    if no == 4:
    	return x*np.tan(np.deg2rad(y))
    if no == 5:
    	return x*np.tan(np.deg2rad(y))

def constrainedPts(points, const, constVal, compMode):
    """Function that will constraint points out of bounds
    
    INPUTS:
    points:     points in the parameter search space as a numpy.ndarray
    const:      function with search space components and constraints number
    constVal:   comparison value for each constraint as list
    compMode:   comparison mode ('leq','geq','less','greater','equal') as list
    
    OUTPUTS:
    booleanMat: boolean matrix with 1 for the non valid points (constrained)
    
    This function will evaluate the constraints for all points in the set returning a 
    boolean masked matrix with the values that are constrained. It will raise an error
    in there is something wrong with the comparison mode. 
    """
    
    #Let's create a function that checks if any of the points is constrained and returns its boolean
    boolMat = np.zeros([len(constVal), points.shape[0]])
    #Let's get the points that are valid under the constraints
    for i in range(len(constVal)):
        if compMode[i] == 'leq':
            boolMat[i,:] = np.logical_or(const(points[:,0], points[:,1], i) < constVal[i],
                                         const(points[:,0], points[:,1], i) == constVal[i])
        elif compMode[i] == 'less':
            boolMat[i,:] = const(points[:,0], points[:,1], i) < constVal[i]
        elif compMode[i] == 'geq':
            boolMat[i,:] = np.logical_or(const(points[:,0], points[:,1], i) > constVal[i], 
                                         const(points[:,0], points[:,1], i) == constVal[i])
        elif compMode[i] == 'greater':
            boolMat[i,:] = const(points[:,0], points[:,1], i) > constVal[i]
        elif compMode[i] == 'eq':
            boolMat[i,:] = const(points[:,0], points[:,1], i) == constVal[i]
        else:
            raise RuntimeError('Bad comparison mode matrix')
    #Once all the comparisons are made, the output should be an OR array along the boolMat
    return np.logical_or.reduce(np.logical_not(boolMat))