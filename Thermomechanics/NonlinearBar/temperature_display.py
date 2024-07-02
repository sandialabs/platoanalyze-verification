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
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

animationScene1.GoToLast()

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
temperatureLUT.RGBPoints = [-2.032606154049026e-12, 0.231373, 0.298039, 0.752941, 125.00000000085097, 0.865003, 0.865003, 0.865003, 250.00000000170397, 0.705882, 0.0156863, 0.14902]
temperatureLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for temperatureLUT in view renderView1
temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)
temperatureLUTColorBar.Title = 'temperature'
temperatureLUTColorBar.ComponentTitle = ''

# change scalar bar placement
temperatureLUTColorBar.Orientation = 'Horizontal'
temperatureLUTColorBar.WindowLocation = 'AnyLocation'
temperatureLUTColorBar.Position = [0.3358964879852125, 0.2499507389162562]
temperatureLUTColorBar.ScalarBarLength = 0.3299999999999997

# current camera placement for renderView1
renderView1.CameraPosition = [0.7878634085400765, 0.6980282221737437, 1.3065466273925788]
renderView1.CameraFocalPoint = [-0.06720160103207375, -0.23929430901196236, -0.15666947561469705]
renderView1.CameraViewUp = [-0.25669425979074656, 0.8749839285415836, -0.41050113493682056]
renderView1.CameraParallelScale = 0.5012484414312457

# save screenshot
SaveScreenshot('./Thermomechanics_NonlinearBar_temperature_solution.png', renderView1, ImageResolution=[1195, 536])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.7878634085400765, 0.6980282221737437, 1.3065466273925788]
renderView1.CameraFocalPoint = [-0.06720160103207375, -0.23929430901196236, -0.15666947561469705]
renderView1.CameraViewUp = [-0.25669425979074656, 0.8749839285415836, -0.41050113493682056]
renderView1.CameraParallelScale = 0.5012484414312457

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
