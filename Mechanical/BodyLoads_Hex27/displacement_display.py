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
outputexoDisplay.ScaleFactor = 0.5
outputexoDisplay.SelectScaleArray = 'GlobalNodeId'
outputexoDisplay.GlyphType = 'Arrow'
outputexoDisplay.GlyphTableIndexArray = 'GlobalNodeId'
outputexoDisplay.DataAxesGrid = 'GridAxesRepresentation'
outputexoDisplay.PolarAxes = 'PolarAxesRepresentation'
outputexoDisplay.ScalarOpacityUnitDistance = 0.27595807455445465

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

# get color legend/bar for displacementLUT in view renderView1
displacementLUTColorBar = GetScalarBar(displacementLUT, renderView1)

# change scalar bar placement
displacementLUTColorBar.Orientation = 'Horizontal'
displacementLUTColorBar.WindowLocation = 'AnyLocation'
displacementLUTColorBar.Position = [0.34975970425138614, 0.14034482758620698]
displacementLUTColorBar.ScalarBarLength = 0.3300000000000004

# change scalar bar placement
displacementLUTColorBar.ScalarBarLength = 0.4214972273567471

# change scalar bar placement
displacementLUTColorBar.Position = [0.31648798521256916, 0.14157635467980306]

# current camera placement for renderView1
renderView1.CameraPosition = [4.548096653382324, 2.107962970831805, 5.948811494335789]
renderView1.CameraFocalPoint = [-1.0316841958882286, -1.1589274238092677, -1.7296547996499312]
renderView1.CameraViewUp = [-0.18445308059068502, 0.9455266777836733, -0.2682468315935458]
renderView1.CameraParallelScale = 2.598076211353316

# save screenshot
SaveScreenshot('./BodyLoads_Hex27_solution.png', renderView1, ImageResolution=[1324, 802])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [4.548096653382324, 2.107962970831805, 5.948811494335789]
renderView1.CameraFocalPoint = [-1.0316841958882286, -1.1589274238092677, -1.7296547996499312]
renderView1.CameraViewUp = [-0.18445308059068502, 0.9455266777836733, -0.2682468315935458]
renderView1.CameraParallelScale = 2.598076211353316

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
