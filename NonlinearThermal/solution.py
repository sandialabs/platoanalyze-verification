#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
stepspvd = PVDReader(FileName='./output_data/steps.pvd')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [1225, 800]

# show data in view
stepspvdDisplay = Show(stepspvd, renderView1)
# trace defaults for the display properties.
stepspvdDisplay.Representation = 'Surface'
stepspvdDisplay.ColorArrayName = [None, '']
stepspvdDisplay.OSPRayScaleArray = 'Temperature'
stepspvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
stepspvdDisplay.SelectOrientationVectors = 'None'
stepspvdDisplay.ScaleFactor = 0.2
stepspvdDisplay.SelectScaleArray = 'None'
stepspvdDisplay.GlyphType = 'Arrow'
stepspvdDisplay.GlyphTableIndexArray = 'None'
stepspvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
stepspvdDisplay.PolarAxes = 'PolarAxesRepresentation'
stepspvdDisplay.ScalarOpacityUnitDistance = 0.04661854730260802

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

# change representation type
stepspvdDisplay.SetRepresentationType('Surface With Edges')

# Rescale transfer function
temperatureLUT.RescaleTransferFunction(0.0, 0.002)

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')

# Rescale transfer function
temperaturePWF.RescaleTransferFunction(0.0, 0.002)

# current camera placement for renderView1
renderView1.CameraPosition = [1.7438733200602154, 1.1546006004002538, 2.4716222099918332]
renderView1.CameraFocalPoint = [0.09698992820004326, -0.16428522011225666, 0.023257295123646403]
renderView1.CameraViewUp = [-0.19924057811635842, 0.9124190832933381, -0.3574837177746757]
renderView1.CameraParallelScale = 1.224744871391589

# save screenshot
SaveScreenshot('NonlinearThermal_solution.png', renderView1, ImageResolution=[1225, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.7438733200602154, 1.1546006004002538, 2.4716222099918332]
renderView1.CameraFocalPoint = [0.09698992820004326, -0.16428522011225666, 0.023257295123646403]
renderView1.CameraViewUp = [-0.19924057811635842, 0.9124190832933381, -0.3574837177746757]
renderView1.CameraParallelScale = 1.224744871391589

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
