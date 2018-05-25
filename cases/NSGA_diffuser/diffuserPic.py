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

# Go to the last available timestep
animationScene1.GoToLast()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# Set a specific view size
renderView1.ViewSize = [750, 500]

# Compute the derivatives of the fields
computeDerivatives1 = ComputeDerivatives(Input=case)
computeDerivatives1.Vectors = ['POINTS', 'U']
computeDerivatives1.Scalars = ['POINTS', 'rho']
computeDerivatives1.OutputTensorType = 'Nothing'

# Covert Cell-Data to Point-Data
cellDatatoPointData1 = CellDatatoPointData(Input=computeDerivatives1)

# Show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# Set scalar coloring
ColorBy(cellDatatoPointData1Display, ('POINTS', 'ScalarGradient', 'Magnitude'))

# Rescale the color map used to include current data range
cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

# Show color bar and color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# Get color map for the ScalarGradient
scalarGradientLUT = GetColorTransferFunction('ScalarGradient')
scalarGradientLUT.RescaleTransferFunction(0.0, 3.0)
scalarGradientLUT.ApplyPreset('X Ray', True)

# Get colorbar for scalarGradientLUT in view renderView1
scalarGradientLUTColorBar = GetScalarBar(scalarGradientLUT, renderView1)
scalarGradientLUTColorBar.Title = 'Density'
scalarGradientLUTColorBar.ComponentTitle = 'Gradient'
scalarGradientLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
scalarGradientLUTColorBar.Orientation = 'Horizontal'
scalarGradientLUTColorBar.WindowLocation = 'AnyLocation'
scalarGradientLUTColorBar.Position = [0.3481150159744408, 0.16036697247706422]
scalarGradientLUTColorBar.ScalarBarLength = 0.35
scalarGradientLUTColorBar.AddRangeLabels = 0

# Change the background color
renderView1.Background = [1.0, 1.0, 1.0]

# Placement of the camera for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [3.7086592114601054, 0.6190414490504583, 10.802519721951658]
renderView1.CameraFocalPoint = [3.7086592114601054, 0.6190414490504583, 0.05000000074505806]
renderView1.CameraParallelScale = 2.2999643691642264
renderView1.CameraViewAngle = 26

# Save screenshot
SaveScreenshot('./gen%i/data/SCg%ii%i.png' %(gen, gen, ind), renderView1, ImageResolution=[750, 500])