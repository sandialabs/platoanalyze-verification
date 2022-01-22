#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
stepspvd = PVDReader(FileName='output_data/steps.pvd')

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
stepspvdDisplay.ScalarOpacityUnitDistance = 0.02063035542972885

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

animationScene1.GoToLast()

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'total displacement', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stepspvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'totaldisplacement'
totaldisplacementLUT = GetColorTransferFunction('totaldisplacement')

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=stepspvd)
warpByVector1.Vectors = ['POINTS', 'Displacements']

# Properties modified on warpByVector1
warpByVector1.ScaleFactor = 5.0

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
warpByVector1Display.ScaleFactor = 0.10000000000000203
warpByVector1Display.SelectScaleArray = 'Displacements'
warpByVector1Display.GlyphType = 'Arrow'
warpByVector1Display.GlyphTableIndexArray = 'Displacements'
warpByVector1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByVector1Display.PolarAxes = 'PolarAxesRepresentation'
warpByVector1Display.ScalarOpacityFunction = totaldisplacementPWF
warpByVector1Display.ScalarOpacityUnitDistance = 0.020630355429729047

# hide data in view
Hide(stepspvd, renderView1)

# show color bar/color legend
warpByVector1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# change representation type
warpByVector1Display.SetRepresentationType('Surface With Edges')

# get color legend/bar for totaldisplacementLUT in view renderView1
totaldisplacementLUTColorBar = GetScalarBar(totaldisplacementLUT, renderView1)

# change scalar bar placement
totaldisplacementLUTColorBar.WindowLocation = 'AnyLocation'
totaldisplacementLUTColorBar.Position = [0.8352402745995424, 0.27355623100303955]
totaldisplacementLUTColorBar.ScalarBarLength = 0.33000000000000024

# current camera placement for renderView1
renderView1.CameraPosition = [1.722204564497744, -2.591482755752237, 1.6142133569469523]
renderView1.CameraFocalPoint = [0.039727478234983155, -0.07495088024738139, 0.18855891197246466]
renderView1.CameraViewUp = [-0.25884551755577384, 0.33928356380543473, 0.904370312080603]
renderView1.CameraParallelScale = 0.8660254037844386

# save screenshot
SaveScreenshot('4LayerNormal_solution.png', renderView1, ImageResolution=[1200, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.722204564497744, -2.591482755752237, 1.6142133569469523]
renderView1.CameraFocalPoint = [0.039727478234983155, -0.07495088024738139, 0.18855891197246466]
renderView1.CameraViewUp = [-0.25884551755577384, 0.33928356380543473, 0.904370312080603]
renderView1.CameraParallelScale = 0.8660254037844386

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
