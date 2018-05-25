# Package importation
import numpy as np
import sys
import os
from scipy import integrate

################################################################################
#                                    INPUTS                                    # 
################################################################################
# Get the inputs from the terminal line
gen = int(sys.argv[1])
ind = int(sys.argv[2])
x_cent = float(sys.argv[3])
y_cent = float(sys.argv[4])

################################################################################
#                              FUNCTION DEFINITION                             # 
################################################################################
def joukowsky(x_cent,y_cent):
    '''Joukowsky airfoil components calculation (fixed radius)
    
    INPUTS:
    x_cent: float with the x-position of the center
    y_cent: float with the y-position of the center
    
    OUTPUT:
    x1:     cartesian coordinates for horizontal axis
    y1:     cartesian coordinates for vertical axis
    
    This function computes the cartesian coordinates of a Joukowsky 
    airfoil from the position of the center, having always the radius
    fixed so it can go through the points |0,1|
    '''
    
    # Circle parameters definition
    center = np.array([x_cent,y_cent])
    radius1 = np.sqrt((center[0]-1)**2+(center[1]-0)**2)
    # Second circle will be neglected

    # Circle coordinates calculations
    angle = np.linspace(0,2*np.pi,500)
    chi1 = center[0] + radius1*np.cos(angle)
    eta1 = center[1] + radius1*np.sin(angle)

    # Cartesian components of the Joukowsky transform
    x1 = ((chi1)*(chi1**2+eta1**2+1))/(chi1**2+eta1**2)
    y1 = ((eta1)*(chi1**2+eta1**2-1))/(chi1**2+eta1**2)

    return x1, y1

def airfoil_correction(x, y):
    '''Set the airfoil chord to 1 and the leading edge to (0,0)
    
    INPUT:
    x:     cartesian coordinates for horizontal axis
    y:     cartesian coordinates for vertical axis
    
    OUTPUT:
    xCorr: corrected cartesian coordinates for horizontal axis
    yCorr: corrected cartesian coordinates for vertical axis
    
    The function scales the airfoil to match the chord dimension to
    a value of 1 (proportionally scaling the vertical dimension). The
    leading edge of the airfoil is moved after to a position in (0,0)
    '''
    # Compute the scale factor (actual chord length)
    c = np.max(x)-np.min(x)
    
    # Leading edge current position
    LE = np.min(x/c)

    # Corrected position of the coordinates
    xCorr = x/c-LE
    yCorr = y/c
    
    return xCorr, yCorr

################################################################################
#                            PARAMETER DECLARATION                             # 
################################################################################
# Reference percentage of the chord
pc = 0.25;

# Airfoil coordinate set of points
xTemp, yTemp = joukowsky(x_cent, y_cent)
x, y = airfoil_correction(xTemp, yTemp)

# Location of the two pc-intercepts for the airfoil
firstPC = np.argwhere(x-pc<0)[0]
lastPC = np.argwhere(x-pc<0)[-1]

# Get the position of the y-intercept point
if np.any(y == 0):
    zeroLoc = np.argwhere(y==0)[1]
else:
    zeroLoc = np.argwhere(y<0)[0]
    
# Depending on the sign of y at pc, get the y-components for the x_pc
if y[lastPC] < 0:
    ypcPos = y[firstPC]
    ypcNeg = y[lastPC]
else:
    ypcPos = y[lastPC]
    ypcNeg = y[firstPC]

# Avoid excessive refinement in the leading edge
y = np.delete(y, np.argwhere(x < 0.0005))
x = np.delete(x, np.argwhere(x < 0.0005))
points = np.vstack((x,y)).T

# Separate between the upper and lower airfoil surfaces
upper = points[:np.argwhere(y < 0)[0][0], :]
lower = points[np.argwhere(y < 0)[0][0]:, :]

# Separate between the 4 quadrants specified with the y = 0 line and the specified pc
UL = upper[upper[:,0]<pc,:]
UR = upper[upper[:,0]>pc,:]
LL = lower[lower[:,0]<pc,:]
LR = lower[lower[:,0]>pc,:]

# Sort the 4 quadrants with increasing x-component
UL = UL[np.argsort(UL[:,0]),:]
UR = UR[np.argsort(UR[:,0]),:]
LL = LL[np.argsort(LL[:,0]),:]
LR = LR[np.argsort(LR[:,0]),:]

# Fix the first and last points of every quadrant
UL[0,:] = np.array([0,0])
UL[-1,:] = np.array([pc,ypcPos])
UR[0,:] = np.array([pc,ypcPos])
UR[-1,:] = np.array([1,0])
LL[0,:] = np.array([0,0])
LL[-1,:] = np.array([pc,ypcNeg])
LR[0,:] = np.array([pc,ypcNeg])
LR[-1,:] = np.array([1,0])

################################################################################
#                               AREA CALCULATION                               # 
################################################################################
# Once the different lines are computed, the area will be computed as the integral of those lines

# In case the lower surface of the airfoil interceps the y = 0 axis, it must be divided so all areas 
# are computed independently
lowerNeg = lower[lower[:,1]<0,:]
lowerPos = lower[lower[:,1]>0,:]

# Upper surface area
A1 = integrate.simps(upper[np.argsort(upper[:,0]),1], upper[np.argsort(upper[:,0]),0])
# Lower surface area for points with negative y
A2 = -integrate.simps(lowerNeg[np.argsort(lowerNeg[:,0]),1], lowerNeg[np.argsort(lowerNeg[:,0]),0])
# Possible lower surface area for points with positive y
A3 = integrate.simps(lowerPos[np.argsort(lowerPos[:,0]),1], lowerPos[np.argsort(lowerPos[:,0]),0])

# The area will be the sum of the areas and substracting the possible intercept of both
area = A1 + A2 - A3 

# Append the area into the FIT file for the generation and individual
with open('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind), "a") as file:
    file.write(str(area))