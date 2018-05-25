# Import the simple module from the paraview and the system package
from paraview.simple import *
import sys

################################################################################
#                                    INPUTS                                    # 
################################################################################
# Get the generation and individual number
gen = int(sys.argv[1])
ind = int(sys.argv[2])

################################################################################
#                                PVBATCH SCRIPT                                # 
################################################################################
# Disable automatic camera reset
paraview.simple._DisableFirstRenderCameraReset()

# Open the OpenFOAM desired file
case = OpenFOAMReader(FileName='./gen%i/ind%i/g%ii%i.OpenFOAM' %(gen, ind, gen, ind))

# Get animation scene
animationScene1 = GetAnimationScene()

# Update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# Set a specific view size
renderView1.ViewSize = [663, 680]

# Show data in view
caseDisplay = Show(case, renderView1)

# Reset view to fit data
renderView1.ResetCamera()

# Update the view to ensure updated data information
renderView1.Update()

# Set scalar coloring
ColorBy(caseDisplay, ('POINTS', 'U', 'Magnitude'))

# Show color bar
caseDisplay.SetScalarBarVisibility(renderView1, True)

# Get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 45.0)

# Go to the last available timestep
animationScene1.GoToLast()

# Get color bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)

# Change scalar bar placement
uLUTColorBar.Orientation = 'Horizontal'
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.5474509803921569, 0.09999999999999999]
uLUTColorBar.ScalarBarLength = 0.33

# Prescribed camera conditions for same POV in all pictures
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.51669332149332, 0.0413887325147504, 39.6239706844175]
renderView1.CameraFocalPoint = [0.51669332149332, 0.0413887325147504, 0.0500000007450581]
renderView1.CameraViewUp = [0.0, 1.0, 0.0]
renderView1.CenterOfRotation = [2.0, 0.0, 0.0500000007450581]
renderView1.RotationFactor = 1.0
renderView1.CameraViewAngle = 4
renderView1.CameraParallelScale = 1.26033555790814
renderView1.CameraParallelProjection = 0

# Make white background
renderView1.Background = [1.0, 1.0, 1.0]

# Update the view to ensure updated data information
renderView1.Update()

# Save screenshot
SaveScreenshot('./gen%i/data/g%ii%i.png' %(gen, gen, ind), renderView1, ImageResolution=[663, 680])