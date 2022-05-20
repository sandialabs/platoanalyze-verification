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
outputexoDisplay.ScaleFactor = 0.1
outputexoDisplay.SelectScaleArray = 'GlobalNodeId'
outputexoDisplay.GlyphType = 'Arrow'
outputexoDisplay.GlyphTableIndexArray = 'GlobalNodeId'
outputexoDisplay.DataAxesGrid = 'GridAxesRepresentation'
outputexoDisplay.PolarAxes = 'PolarAxesRepresentation'
outputexoDisplay.ScalarOpacityUnitDistance = 0.014486369191648989

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
temperatureLUTColorBar.Position = [0.3155637707948243, 0.1612807881773399]
temperatureLUTColorBar.ScalarBarLength = 0.3300000000000001

# current camera placement for renderView1
renderView1.CameraPosition = [0.9216269766250665, 0.6837760189784818, 1.2243747258707847]
renderView1.CameraFocalPoint = [-0.12708846472747892, -0.19147028846658956, -0.24693581424125283]
renderView1.CameraViewUp = [-0.1996754917046382, 0.8980709140800613, -0.3919162299470566]
renderView1.CameraParallelScale = 0.5196152428442091

# save screenshot
SaveScreenshot('./NonlinearThermal_solution.png', renderView1, ImageResolution=[1267, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.9216269766250665, 0.6837760189784818, 1.2243747258707847]
renderView1.CameraFocalPoint = [-0.12708846472747892, -0.19147028846658956, -0.24693581424125283]
renderView1.CameraViewUp = [-0.1996754917046382, 0.8980709140800613, -0.3919162299470566]
renderView1.CameraParallelScale = 0.5196152428442091

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
