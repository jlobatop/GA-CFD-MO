# Package importation
import numpy as np
import sys
import os

# Get the inputs from the terminal line
x_cent = float(sys.argv[1])
y_cent = float(sys.argv[2])

# Delete previous blockMeshDict
os.system("rm ./case/system/blockMeshDict")

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
# Dimensions
pc = 0.25;
r = 6;
l = 10;
maxZ = 0.1;
minZ = 0.0;

# Number of cells
Npre = 110;
Npost = 80;
Nwake = 175;
Ny = 100;
Nz = 1;

# Grading parameters
pre1 = 1;
pre2 = 3.2;
post1 = 1.8;
post2 = 0.5;
wake = 30;
yDir1 = 30;
yDir2 = 1;
zDir = 1;

# Airfoil coordinate dataset
xTemp, yTemp = joukowsky(x_cent, y_cent)
x, y = airfoil_correction(xTemp, yTemp)

# Location of the pc (percentage of the chord) for the circle
firstPC = np.argwhere(x-pc<0)[0]
lastPC = np.argwhere(x-pc<0)[-1]

if np.any(y == 0):
    zeroLoc = np.argwhere(y==0)[1]
else:
    zeroLoc = np.argwhere(y<0)[0]
    
if y[lastPC] < 0:
    # Get the y-component for the x_pc
    ypcPos = y[firstPC]
    ypcNeg = y[lastPC]
else:
    # Get the y-component for the x_pc
    ypcPos = y[lastPC]
    ypcNeg = y[firstPC]

y = np.delete(y, np.argwhere(x < 0.0005))
x = np.delete(x, np.argwhere(x < 0.0005))
points = np.vstack((x,y)).T

upper = points[:np.argwhere(y < 0)[0][0], :]
lower = points[np.argwhere(y < 0)[0][0]:, :]

UL = upper[upper[:,0]<pc,:]
UR = upper[upper[:,0]>pc,:]
LL = lower[lower[:,0]<pc,:]
LR = lower[lower[:,0]>pc,:]

UL = UL[np.argsort(UL[:,0]),:]
UR = UR[np.argsort(UR[:,0]),:]
LL = LL[np.argsort(LL[:,0]),:]
LR = LR[np.argsort(LR[:,0]),:]

UL[0,:] = np.array([0,0])
UL[-1,:] = np.array([pc,ypcPos])
UR[0,:] = np.array([pc,ypcPos])
UR[-1,:] = np.array([1,0])
LL[0,:] = np.array([0,0])
LL[-1,:] = np.array([pc,ypcNeg])
LR[0,:] = np.array([pc,ypcNeg])
LR[-1,:] = np.array([1,0])

################################################################################
#                                   MAIN BODY                                  # 
################################################################################
# Header
bMD0 = """/*--------------------------------*- C++ -*----------------------------------*
| =========                |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  5                                     |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

convertToMeters 1;
"""

# Vertices
bMD1 = """
vertices
(
	($pc	$rNeg 	$minZ)		// point 0
	(1.0 	$rNeg 	$minZ)		// point 1
	($l 	$rNeg 	$minZ)		// point 2
	($pc 	$ypcNeg	$minZ)		// point 3
	($rNeg 	0.0		$minZ)		// point 4
	(0.0 	0.0		$minZ)		// point 5
	(1.0	0.0		$minZ)		// point 6
	($l 	0.0		$minZ)		// point 7
	($pc 	$ypcPos	$minZ)		// point 8
	($pc 	$rPos	$minZ)		// point 9
	(1.0	$rPos	$minZ)		// point 10
	($l 	$rPos	$minZ)		// point 11

	($pc	$rNeg 	$maxZ)		// point 12
	(1.0 	$rNeg 	$maxZ)		// point 13
	($l 	$rNeg 	$maxZ)		// point 14
	($pc 	$ypcNeg	$maxZ)		// point 15
	($rNeg 	0.0		$maxZ)		// point 16
	(0.0 	0.0		$maxZ)		// point 17
	(1.0	0.0		$maxZ)		// point 18
	($l 	0.0		$maxZ)		// point 19
	($pc 	$ypcPos	$maxZ)		// point 20
	($pc 	$rPos	$maxZ)		// point 21
	(1.0	$rPos	$maxZ)		// point 22
	($l 	$rPos	$maxZ)		// point 23
);\n """
   
        	# (0.5 0.65 yDir)
        	# (0.5 0.35 1)
    
# Blocks
bMD2 = """
blocks
(
    hex (17 15 12 16 5 3 0 4) 	($Npre 		$Ny 	$Nz) 	simpleGrading 		// block 0
    ( 
        (
        	(0.5 0.65 $pre1)
        	(0.5 0.35 $pre2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
        	(1 1 $zDir)
        )
    )
    hex (5 8 9 4 17 20 21 16) 	($Npre 		$Ny 	$Nz) 	simpleGrading 		// block 1
    ( 
        (
        	(0.5 0.65 $pre1)
        	(0.5 0.35 $pre2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
        	(1 1 $zDir)
        )
    )
    hex (15 18 13 12 3 6 1 0) 	($Npost 	$Ny 	$Nz) 	simpleGrading 		// block 2
    ( 
        (
        	(0.5 0.45 $post1)
        	(0.5 0.55 $post2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
        	(1 1 $zDir)
        )
    )
    hex (8 6 10 9 20 18 22 21) 	($Npost 	$Ny 	$Nz) 	simpleGrading 		// block 3
    ( 
        (
        	(0.5 0.45 $post1)
        	(0.5 0.55 $post2)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
        	(1 1 $zDir)
        )
    )
    hex (18 19 14 13 6 7 2 1) 	($Nwake 	$Ny 	$Nz) 	simpleGrading 		// block 4
    ( 
        (
        	(1 1 $wake)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
        	(1 1 $zDir)
        )
    )
    hex (6 7 11 10 18 19 23 22)	($Nwake 	$Ny 	$Nz) 	simpleGrading 		// block 5
    ( 
        (
        	(1 1 $wake)
        )
        (
            (0.2 0.5 $yDir1)
            (0.8 0.5 $yDir2)
        )
        (
        	(1 1 $zDir)
        )
    )
); \n
"""
    
# Edges are included below
    
# Boundary
bMD3 = """boundary
(
	inlet
    {
        type patch;
        faces
        (
            (9 21 16 4)
            (4 16 12 0)
        );
    }   

    outlet
    {
        type patch;
        faces
        (
            (23 11 7 19)
            (19 7 2 14)
        );
    }   


    airfoil
    {
        type wall;
        faces
        (
            (8 20 18 6)
            (6 18 15 3)
            (17 5 3 15)
            (20 8 5 17)
        );
    }   

    lower
    {
        type symmetry;
        faces
        (
            (0 12 13 1)
            (1 13 14 2)
        );
    }   

    upper
    {
        type symmetry;
        faces
        (
            (21 9 10 22)
            (22 10 11 23)
        );
    }

);

// ************************************************************************* //
"""
    
# Writing the data in the file
with open('./case/system/blockMeshDict', "a") as bMD:
    # Header
    bMD.write(bMD0)
    
    # Parameters
    bMD.write("pc 			%.8f; \n" %pc)
    bMD.write("rPos		%.8f; \n" %r)
    bMD.write("rNeg 		%.8f; \n" %(-r))
    bMD.write("l			%.8f; \n" %l)
    bMD.write("ypcPos		%.8f; \n" %ypcPos)
    bMD.write("ypcNeg		%.8f; \n" %ypcNeg)
    bMD.write("maxZ		%.8f; \n" %maxZ)
    bMD.write("minZ		%.8f; \n" %minZ)
    bMD.write("circPos		%.8f; \n" %(r*np.cos(np.pi/4)))
    bMD.write("circNeg		%.8f; \n" %(-r*np.cos(np.pi/4)))
    bMD.write("Npre		%i; \n" %Npre)
    bMD.write("Npost		%i; \n" %Npost)
    bMD.write("Nwake		%i; \n" %Nwake)
    bMD.write("Ny		%i; \n" %Ny)
    bMD.write("Nz 			%i; \n" %Nz)
    bMD.write("pre1			%.8f; \n" %pre1)
    bMD.write("pre2			%.8f; \n" %pre2)
    bMD.write("post1		%.8f; \n" %post1)
    bMD.write("post2		%.8f; \n" %post2)
    bMD.write("wake		%.8f; \n" %wake)
    bMD.write("yDir1		%.8f; \n" %yDir1)
    bMD.write("yDir2		%.8f; \n" %yDir2)
    bMD.write("zDir		%.8f; \n" %zDir)

    # Vertices
    bMD.write(bMD1)
    
    # Blocks
    bMD.write(bMD2)
    
    # Edges
    bMD.write("""edges 
(
    // Upper circular inlet
    arc 4  9  ($circNeg $circPos $minZ)
    arc 16 21 ($circNeg $circPos $maxZ)
    
    // Lower circular inlet
    arc 4  0  ($circNeg $circNeg $minZ)
    arc 16 12 ($circNeg $circNeg $maxZ)
    
""");

    # Upper right airfoil
    bMD.write('    // Upper right airfoil\n')  
    bMD.write('    spline 8 6 ( \n')
    for i in range(len(UR)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(UR[i,0], UR[i,1], minZ))
    bMD.write('        ) \n')
    bMD.write('    spline 20 18 ( \n')
    for i in range(len(UR)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(UR[i,0], UR[i,1], maxZ))
    bMD.write('        ) \n')

    # Upper left airfoil
    bMD.write('    // Upper left airfoil\n')  
    bMD.write('    spline 5 8 ( \n')
    for i in range(len(UL)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(UL[i,0], UL[i,1], minZ))
    bMD.write('        ) \n')
    bMD.write('    spline 17 20 ( \n')
    for i in range(len(UL)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(UL[i,0], UL[i,1], maxZ))
    bMD.write('        ) \n')

    # Lower left airfoil
    bMD.write('    // Lower left airfoil\n')
    bMD.write('    spline 5 3 ( \n')
    for i in range(len(LL)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(LL[i,0], LL[i,1], minZ))
    bMD.write('        ) \n')

    bMD.write('    spline 17 15 ( \n')
    for i in range(len(LL)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(LL[i,0], LL[i,1], maxZ))
    bMD.write('        ) \n')

    # Lower right airfoil
    bMD.write('    // Lower right airfoil\n')
    bMD.write('    spline 3 6 ( \n')
    for i in range(len(LR)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(LR[i,0], LR[i,1], minZ))
    bMD.write('        ) \n')

    bMD.write('    spline 15 18 ( \n')
    for i in range(len(LR)):
        bMD.write('        (%.8f %.8f %.8f) \n' %(LR[i,0], LR[i,1], maxZ))
    bMD.write('        ) \n')

    bMD.write(""");
    \n""")
              
    # Boundary 
    bMD.write(bMD3)
        
# blockMesh and paraFoam calling
os.chdir("./case") 
os.system("blockMesh >bmOutput 2>&1")