#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
stepspvd = PVDReader(FileName='./output_data/steps.pvd')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [1267, 800]

# show data in view
stepspvdDisplay = Show(stepspvd, renderView1)
# trace defaults for the display properties.
stepspvdDisplay.Representation = 'Surface'
stepspvdDisplay.ColorArrayName = [None, '']
stepspvdDisplay.OSPRayScaleArray = 'Temperature'
stepspvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
stepspvdDisplay.SelectOrientationVectors = 'None'
stepspvdDisplay.ScaleFactor = 0.1
stepspvdDisplay.SelectScaleArray = 'None'
stepspvdDisplay.GlyphType = 'Arrow'
stepspvdDisplay.GlyphTableIndexArray = 'None'
stepspvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
stepspvdDisplay.PolarAxes = 'PolarAxesRepresentation'
stepspvdDisplay.ScalarOpacityUnitDistance = 0.014486369175659087

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'Temperature'))

# rescale color and/or opacity maps used to include current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stepspvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Temperature'
temperatureLUT = GetColorTransferFunction('Temperature')

# Rescale transfer function
temperatureLUT.RescaleTransferFunction(0.0, 250.0)

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')

# Rescale transfer function
temperaturePWF.RescaleTransferFunction(0.0, 250.0)

# current camera placement for renderView1
renderView1.CameraPosition = [0.8413022880366952, 0.4684080298368859, 0.8265385761620435]
renderView1.CameraFocalPoint = [-0.3444481247560767, -0.3964885446434466, -0.5433390629679448]
renderView1.CameraViewUp = [-0.3076189752826347, 0.901918981966087, -0.303171100231073]
renderView1.CameraParallelScale = 0.5196152422706632

# save screenshot
SaveScreenshot('./Thermomechanics_StaticNonlinearBar_temperature_solution.png', renderView1, ImageResolution=[1267, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.8413022880366952, 0.4684080298368859, 0.8265385761620435]
renderView1.CameraFocalPoint = [-0.3444481247560767, -0.3964885446434466, -0.5433390629679448]
renderView1.CameraViewUp = [-0.3076189752826347, 0.901918981966087, -0.303171100231073]
renderView1.CameraParallelScale = 0.5196152422706632

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
