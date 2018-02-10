#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get number of timesteps to iterate over
tsNo = raw_input('Number of timesteps: ')

# get active source.
plotOverLine1 = GetActiveSource()

# get display properties
plotOverLine1Display = GetDisplayProperties(plotOverLine1, view=renderView1)

# set scalar coloring
ColorBy(plotOverLine1Display, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
plotOverLine1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
plotOverLine1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# find view
lineChartView1 = FindViewOrCreate('LineChartView1', viewtype='XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [808, 714]

# set active view
SetActiveView(lineChartView1)

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToNext()

# save data
SaveData('./1.csv', proxy=plotOverLine1)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).