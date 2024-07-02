#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'ExodusIIReader'
outputexo = ExodusIIReader(FileName=['./output_data.exo'])
outputexo.PointVariables = []
outputexo.SideSetArrayStatus = []
outputexo.NodeMapArrayStatus = ['Unnamed map ID: -1']
outputexo.ElementMapArrayStatus = ['Unnamed map ID: -1']

# Properties modified on outputexo
outputexo.PointVariables = ['temperature']
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
outputexoDisplay.ScaleFactor = 0.2
outputexoDisplay.SelectScaleArray = 'GlobalNodeId'
outputexoDisplay.GlyphType = 'Arrow'
outputexoDisplay.GlyphTableIndexArray = 'GlobalNodeId'
outputexoDisplay.DataAxesGrid = 'GridAxesRepresentation'
outputexoDisplay.PolarAxes = 'PolarAxesRepresentation'
outputexoDisplay.ScalarOpacityUnitDistance = 0.04661854730260802

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
ColorBy(outputexoDisplay, ('POINTS', 'temperature'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
outputexoDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'temperature'
temperatureLUT = GetColorTransferFunction('temperature')

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)

# change scalar bar placement
temperatureLUTColorBar.Orientation = 'Horizontal'
temperatureLUTColorBar.WindowLocation = 'AnyLocation'
temperatureLUTColorBar.Position = [0.3636229205175603, 0.07999999999999978]
temperatureLUTColorBar.ScalarBarLength = 0.32999999999999985

# current camera placement for renderView1
renderView1.CameraPosition = [1.5711343326076652, -3.5934340179274016, 1.8480350505821843]
renderView1.CameraFocalPoint = [-0.12389660748218705, 0.17029516369075967, -0.4657319223403389]
renderView1.CameraViewUp = [-0.2214910389706495, 0.4363652169892743, 0.8720820586720069]
renderView1.CameraParallelScale = 1.224744871391589

# save screenshot
SaveScreenshot('LinearThermal_solution.png', renderView1, ImageResolution=[1225, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.5711343326076652, -3.5934340179274016, 1.8480350505821843]
renderView1.CameraFocalPoint = [-0.12389660748218705, 0.17029516369075967, -0.4657319223403389]
renderView1.CameraViewUp = [-0.2214910389706495, 0.4363652169892743, 0.8720820586720069]
renderView1.CameraParallelScale = 1.224744871391589

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
