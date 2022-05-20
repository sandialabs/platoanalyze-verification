#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'ExodusIIReader'
outputexo = ExodusIIReader(FileName=['output_data.exo'])
outputexo.ElementVariables = []
outputexo.PointVariables = []
outputexo.SideSetArrayStatus = []
outputexo.NodeMapArrayStatus = ['Unnamed map ID: -1']
outputexo.ElementMapArrayStatus = ['Unnamed map ID: -1']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on outputexo
outputexo.PointVariables = ['total displacement ']
outputexo.ElementBlocks = ['Unnamed block ID: 1 Type: TET4', 'Unnamed block ID: 2 Type: TET4']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1082, 812]

# show data in view
outputexoDisplay = Show(outputexo, renderView1)
# trace defaults for the display properties.
outputexoDisplay.Representation = 'Surface'
outputexoDisplay.ColorArrayName = [None, '']
outputexoDisplay.OSPRayScaleArray = 'GlobalNodeId'
outputexoDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
outputexoDisplay.SelectOrientationVectors = 'GlobalNodeId'
outputexoDisplay.ScaleFactor = 0.1
outputexoDisplay.SelectScaleArray = 'GlobalNodeId'
outputexoDisplay.GlyphType = 'Arrow'
outputexoDisplay.GlyphTableIndexArray = 'GlobalNodeId'
outputexoDisplay.DataAxesGrid = 'GridAxesRepresentation'
outputexoDisplay.PolarAxes = 'PolarAxesRepresentation'
outputexoDisplay.ScalarOpacityUnitDistance = 0.02063035542972885

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(outputexoDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
outputexoDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# set scalar coloring
ColorBy(outputexoDisplay, ('POINTS', 'total displacement ', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
outputexoDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'totaldisplacement'
totaldisplacementLUT = GetColorTransferFunction('totaldisplacement')

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(False, True)

# current camera placement for renderView1
renderView1.CameraPosition = [2.5756047098517847, -1.858144789255512, 1.3034280912612772]
renderView1.CameraFocalPoint = [-1.7028279113782758e-17, 1.2250125384314208e-16, 0.25000000000000017]
renderView1.CameraViewUp = [-0.24843509768879152, 0.19369923922501667, 0.9490840884558178]
renderView1.CameraParallelScale = 0.8660254037844386

# save screenshot
SaveScreenshot('4LayerNormal_solution.png', renderView1, ImageResolution=[1200, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [2.5756047098517847, -1.858144789255512, 1.3034280912612772]
renderView1.CameraFocalPoint = [-1.7028279113782758e-17, 1.2250125384314208e-16, 0.25000000000000017]
renderView1.CameraViewUp = [-0.24843509768879152, 0.19369923922501667, 0.9490840884558178]
renderView1.CameraParallelScale = 0.8660254037844386

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
