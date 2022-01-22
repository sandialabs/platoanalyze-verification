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
# uncomment following to set a specific view size
# renderView1.ViewSize = [874, 658]

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
stepspvdDisplay.ScalarOpacityUnitDistance = 0.027382471108477996

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# change representation type
stepspvdDisplay.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'total displacement', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stepspvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'totaldisplacement'
totaldisplacementLUT = GetColorTransferFunction('totaldisplacement')

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(False, True)

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'total displacement', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(totaldisplacementLUT, stepspvdDisplay)

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=stepspvd)
warpByVector1.Vectors = ['POINTS', 'Displacements']

# Properties modified on warpByVector1
warpByVector1.ScaleFactor = 2.0

# get opacity transfer function/opacity map for 'totaldisplacement'
totaldisplacementPWF = GetOpacityTransferFunction('totaldisplacement')

# show data in view
warpByVector1Display = Show(warpByVector1, renderView1)
# trace defaults for the display properties.
warpByVector1Display.Representation = 'Surface'
warpByVector1Display.ColorArrayName = ['POINTS', 'total displacement']
warpByVector1Display.LookupTable = totaldisplacementLUT
warpByVector1Display.OSPRayScaleArray = 'Displacements'
warpByVector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByVector1Display.SelectOrientationVectors = 'Displacements'
warpByVector1Display.ScaleFactor = 0.10000000000000005
warpByVector1Display.SelectScaleArray = 'Displacements'
warpByVector1Display.GlyphType = 'Arrow'
warpByVector1Display.GlyphTableIndexArray = 'Displacements'
warpByVector1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByVector1Display.PolarAxes = 'PolarAxesRepresentation'
warpByVector1Display.ScalarOpacityFunction = totaldisplacementPWF
warpByVector1Display.ScalarOpacityUnitDistance = 0.02738247110847801

# hide data in view
Hide(stepspvd, renderView1)

# show color bar/color legend
warpByVector1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# change representation type
warpByVector1Display.SetRepresentationType('Surface With Edges')

# Properties modified on warpByVector1
warpByVector1.ScaleFactor = 1.0

# update the view to ensure updated data information
renderView1.Update()

# get color legend/bar for totaldisplacementLUT in view renderView1
totaldisplacementLUTColorBar = GetScalarBar(totaldisplacementLUT, renderView1)

# change scalar bar placement
totaldisplacementLUTColorBar.Orientation = 'Horizontal'
totaldisplacementLUTColorBar.WindowLocation = 'AnyLocation'
totaldisplacementLUTColorBar.Position = [0.31816933638443934, 0.032887537993921044]
totaldisplacementLUTColorBar.ScalarBarLength = 0.33000000000000007

# Properties modified on warpByVector1
warpByVector1.ScaleFactor = 1.0

# update the view to ensure updated data information
renderView1.Update()

# current camera placement for renderView1
renderView1.CameraPosition = [0.8121377934484242, -1.640467178292133, 0.5241407005350806]
renderView1.CameraFocalPoint = [-0.0549020657702766, -0.09598055933174379, -0.14941388841152117]
renderView1.CameraViewUp = [-0.15335049006569385, 0.32142256875491204, 0.9344362789894266]
renderView1.CameraParallelScale = 0.7180703308172536

# save screenshot
SaveScreenshot('2LayerShear_solution.png', renderView1, ImageResolution=[1225, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.8121377934484242, -1.640467178292133, 0.5241407005350806]
renderView1.CameraFocalPoint = [-0.0549020657702766, -0.09598055933174379, -0.14941388841152117]
renderView1.CameraViewUp = [-0.15335049006569385, 0.32142256875491204, 0.9344362789894266]
renderView1.CameraParallelScale = 0.7180703308172536

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
