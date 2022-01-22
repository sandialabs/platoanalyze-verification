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
stepspvdDisplay.OSPRayScaleArray = 'Displacements'
stepspvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
stepspvdDisplay.SelectOrientationVectors = 'Displacements'
stepspvdDisplay.ScaleFactor = 0.1
stepspvdDisplay.SelectScaleArray = 'Displacements'
stepspvdDisplay.GlyphType = 'Arrow'
stepspvdDisplay.GlyphTableIndexArray = 'Displacements'
stepspvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
stepspvdDisplay.PolarAxes = 'PolarAxesRepresentation'
stepspvdDisplay.ScalarOpacityUnitDistance = 0.04663617096453904

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'Temperature'))

# rescale color and/or opacity maps used to include current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stepspvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Temperature'
temperatureLUT = GetColorTransferFunction('Temperature')

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)

# change scalar bar placement
temperatureLUTColorBar.Orientation = 'Horizontal'
temperatureLUTColorBar.WindowLocation = 'AnyLocation'
temperatureLUTColorBar.Position = [0.26058577405857736, 0.10261194029850748]
temperatureLUTColorBar.ScalarBarLength = 0.3299999999999998

# Rescale transfer function
temperatureLUT.RescaleTransferFunction(0.0, 250.0)

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')

# Rescale transfer function
temperaturePWF.RescaleTransferFunction(0.0, 250.0)

# current camera placement for renderView1
renderView1.CameraPosition = [0.5704820647332044, 0.21512831124928153, 0.4395796042443254]
renderView1.CameraFocalPoint = [-0.5794285810586807, -0.5288434615798197, -0.9296985156183778]
renderView1.CameraViewUp = [-0.2756118805638754, 0.922620680174131, -0.26983174721864767]
renderView1.CameraParallelScale = 0.5012484413940855

# save screenshot
SaveScreenshot('./Thermomechanics_NonlinearBar_temperature_solution.png', renderView1, ImageResolution=[1195, 536])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.5704820647332044, 0.21512831124928153, 0.4395796042443254]
renderView1.CameraFocalPoint = [-0.5794285810586807, -0.5288434615798197, -0.9296985156183778]
renderView1.CameraViewUp = [-0.2756118805638754, 0.922620680174131, -0.26983174721864767]
renderView1.CameraParallelScale = 0.5012484413940855

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
