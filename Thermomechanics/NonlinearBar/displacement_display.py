#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'ExodusIIReader'
outputexo = ExodusIIReader(FileName=['./output_data.exo'])
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
outputexo.PointVariables = ['displacement ']
outputexo.ApplyDisplacements = 0
outputexo.ElementBlocks = ['Unnamed block ID: 1 Type: TET4']

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
outputexoDisplay.ScalarOpacityUnitDistance = 0.04663617096799642

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
ColorBy(outputexoDisplay, ('POINTS', 'displacement ', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
outputexoDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'displacement'
displacementLUT = GetColorTransferFunction('displacement')

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(False, True)

# get color legend/bar for displacementLUT in view renderView1
displacementLUTColorBar = GetScalarBar(displacementLUT, renderView1)

# change scalar bar placement
displacementLUTColorBar.Orientation = 'Horizontal'
displacementLUTColorBar.WindowLocation = 'AnyLocation'
displacementLUTColorBar.Position = [0.3248059149722735, 0.203152709359606]
displacementLUTColorBar.ScalarBarLength = 0.3300000000000002

# current camera placement for renderView1
renderView1.CameraPosition = [0.749137666094873, 0.5219484802419891, 1.2023958584836372]
renderView1.CameraFocalPoint = [-0.13859159561069417, -0.24344373521534324, -0.3392988507865966]
renderView1.CameraViewUp = [-0.2803985578239244, 0.9142531842778041, -0.2924342042377378]
renderView1.CameraParallelScale = 0.5012484414312457

# save screenshot
SaveScreenshot('./Thermomechanics_NonlinearBar_displacement_solution.png', renderView1, ImageResolution=[1195, 536])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.749137666094873, 0.5219484802419891, 1.2023958584836372]
renderView1.CameraFocalPoint = [-0.13859159561069417, -0.24344373521534324, -0.3392988507865966]
renderView1.CameraViewUp = [-0.2803985578239244, 0.9142531842778041, -0.2924342042377378]
renderView1.CameraParallelScale = 0.5012484414312457

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
