#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
stepspvd = PVDReader(FileName='./output_data/steps.pvd')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1324, 802]

# show data in view
stepspvdDisplay = Show(stepspvd, renderView1)
# trace defaults for the display properties.
stepspvdDisplay.Representation = 'Surface'
stepspvdDisplay.ColorArrayName = [None, '']
stepspvdDisplay.OSPRayScaleArray = 'Displacements'
stepspvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
stepspvdDisplay.SelectOrientationVectors = 'Displacements'
stepspvdDisplay.ScaleFactor = 0.5
stepspvdDisplay.SelectScaleArray = 'Displacements'
stepspvdDisplay.GlyphType = 'Arrow'
stepspvdDisplay.GlyphTableIndexArray = 'Displacements'
stepspvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
stepspvdDisplay.PolarAxes = 'PolarAxesRepresentation'
stepspvdDisplay.ScalarOpacityUnitDistance = 0.27595807455445465

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# change representation type
stepspvdDisplay.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'Displacements', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
stepspvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Displacements'
displacementsLUT = GetColorTransferFunction('Displacements')

# set scalar coloring
ColorBy(stepspvdDisplay, ('POINTS', 'Displacements', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
stepspvdDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(displacementsLUT, stepspvdDisplay)

# get color legend/bar for displacementsLUT in view renderView1
displacementsLUTColorBar = GetScalarBar(displacementsLUT, renderView1)

# change scalar bar placement
displacementsLUTColorBar.Orientation = 'Horizontal'
displacementsLUTColorBar.WindowLocation = 'AnyLocation'
displacementsLUTColorBar.Position = [0.3625981873111782, 0.06129675810473806]
displacementsLUTColorBar.ScalarBarLength = 0.33000000000000007

# current camera placement for renderView1
renderView1.CameraPosition = [3.2245577716094815, 2.6532503046952387, 5.2324993347044515]
renderView1.CameraFocalPoint = [-0.5918014551294524, -0.8246648975310019, -1.2608521016380025]
renderView1.CameraViewUp = [-0.23015077254034955, 0.9076887147121063, -0.3509014378473888]
renderView1.CameraParallelScale = 2.598076211353316

# save screenshot
SaveScreenshot('./Assemblies_CompliantContact_solution.png', renderView1, ImageResolution=[1324, 802])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [3.2245577716094815, 2.6532503046952387, 5.2324993347044515]
renderView1.CameraFocalPoint = [-0.5918014551294524, -0.8246648975310019, -1.2608521016380025]
renderView1.CameraViewUp = [-0.23015077254034955, 0.9076887147121063, -0.3509014378473888]
renderView1.CameraParallelScale = 2.598076211353316

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
