#### import the simple module from the paraview
from paraview.simple import *
import sys
import numpy as np

# Get the inputs from the terminal line
gen = int(sys.argv[1])
ind = int(sys.argv[2])
L = float(sys.argv[3])
theta = float(sys.argv[4])

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

## Load the case
case_foam = OpenFOAMReader( FileName='./gen%i/ind%i/g%ii%i.OpenFOAM' %(gen, ind, gen, ind))

# get active source.
case = GetActiveSource()

# get animation scene
animationScene1 = GetAnimationScene()

# go to the last timestep
# animationScene1.GoToLast()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=case,
    Source='High Resolution Line Source')

# Properties modified on plotOverLine1
plotOverLine1.Tolerance = 2.22044604925031e-16

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [4+L*np.cos(np.deg2rad(theta)), 0.8, 0.1]
plotOverLine1.Source.Point2 = [4+L*np.cos(np.deg2rad(theta)), 0.1, 0.1]

# Save data
SaveData('./gen%i/ind%i/DIFFg%ii%i.csv' %(gen, ind, gen, ind), proxy=plotOverLine1)

