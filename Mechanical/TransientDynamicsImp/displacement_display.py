#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
stepspvd = PVDReader(FileName='./output_data/steps.pvd')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.ViewSize = [1195, 536]

# show data in view
stepspvdDisplay = Show(stepspvd, renderView1)
# trace defaults for the display properties.
stepspvdDisplay.Representation = 'Surface'
stepspvdDisplay.ColorArrayName = [None, '']
stepspvdDisplay.OSPRayScaleArray = 'displacement'
stepspvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
stepspvdDisplay.SelectOrientationVectors = 'displacement'
stepspvdDisplay.ScaleFactor = 0.1
stepspvdDisplay.SelectScaleArray = 'displacement'
stepspvdDisplay.GlyphType = 'Arrow'
stepspvdDisplay.GlyphTableIndexArray = 'displacement'
stepspvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
stepspvdDisplay.PolarAxes = 'PolarAxesRepresentation'
stepspvdDisplay.ScalarOpacityUnitDistance = 0.018499393455522487

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'displacement', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stepspvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'displacement'
displacementLUT = GetColorTransferFunction('displacement')

# get color legend/bar for displacementLUT in view renderView1
displacementLUTColorBar = GetScalarBar(displacementLUT, renderView1)

# change scalar bar placement
displacementLUTColorBar.Orientation = 'Horizontal'
displacementLUTColorBar.WindowLocation = 'AnyLocation'
displacementLUTColorBar.Position = [0.317489539748954, 0.07253731343283587]
displacementLUTColorBar.ScalarBarLength = 0.32999999999999996

# Rescale transfer function
displacementLUT.RescaleTransferFunction(0.0, 0.0008)

# get opacity transfer function/opacity map for 'displacement'
displacementPWF = GetOpacityTransferFunction('displacement')

# Rescale transfer function
displacementPWF.RescaleTransferFunction(0.0, 0.0008)

# change scalar bar placement
displacementLUTColorBar.Position = [0.221255230125523, 0.07253731343283587]
displacementLUTColorBar.ScalarBarLength = 0.42623430962343095

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'displacement', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(displacementLUT, stepspvdDisplay)

# Rescale transfer function
displacementLUT.RescaleTransferFunction(0.0, 0.0008)

# Rescale transfer function
displacementPWF.RescaleTransferFunction(0.0, 0.0008)

# current camera placement for renderView1
renderView1.CameraPosition = [0.5206207306783589, 0.2585165430084527, 0.5443285229328163]
renderView1.CameraFocalPoint = [-0.46478766622574985, -0.5091155866919678, -0.9356789994700894]
renderView1.CameraViewUp = [-0.25945010831600723, 0.9170300598662305, -0.3028886108729578]
renderView1.CameraParallelScale = 0.5012484413940855

# save screenshot
SaveScreenshot('TransientDynamicsImp_solution.png', renderView1, ImageResolution=[1195, 536])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.5206207306783589, 0.2585165430084527, 0.5443285229328163]
renderView1.CameraFocalPoint = [-0.46478766622574985, -0.5091155866919678, -0.9356789994700894]
renderView1.CameraViewUp = [-0.25945010831600723, 0.9170300598662305, -0.3028886108729578]
renderView1.CameraParallelScale = 0.5012484413940855

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
