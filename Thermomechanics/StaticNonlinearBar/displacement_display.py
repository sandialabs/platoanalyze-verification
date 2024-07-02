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

# Properties modified on outputexo
outputexo.PointVariables = ['displacement ']
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
outputexoDisplay.ScalarOpacityUnitDistance = 0.018500133188341445

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
displacementLUTColorBar.Position = [0.31926062846580405, 0.19945812807881763]
displacementLUTColorBar.ScalarBarLength = 0.3300000000000003

# current camera placement for renderView1
renderView1.CameraPosition = [0.8093862799270872, 0.9275566756336354, 1.0667682630874689]
renderView1.CameraFocalPoint = [-0.07256196228368601, -0.3265469401786661, -0.11661774530284426]
renderView1.CameraViewUp = [-0.27665416101114854, 0.755245356409497, -0.5941943510477943]
renderView1.CameraParallelScale = 0.5012684847497471

# save screenshot
SaveScreenshot('./Thermomechanics_StaticNonlinearBar_displacement_solution.png', renderView1, ImageResolution=[1195, 536])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.8093862799270872, 0.9275566756336354, 1.0667682630874689]
renderView1.CameraFocalPoint = [-0.07256196228368601, -0.3265469401786661, -0.11661774530284426]
renderView1.CameraViewUp = [-0.27665416101114854, 0.755245356409497, -0.5941943510477943]
renderView1.CameraParallelScale = 0.5012684847497471

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
