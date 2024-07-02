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

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on outputexo
outputexo.PointVariables = ['total displacement ']
outputexo.ElementBlocks = ['Unnamed block ID: 1 Type: TET4', 'Unnamed block ID: 2 Type: TET4']

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
outputexoDisplay.ScalarOpacityUnitDistance = 0.027382471108477996

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
ColorBy(outputexoDisplay, ('POINTS', 'total displacement ', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
outputexoDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'totaldisplacement'
totaldisplacementLUT = GetColorTransferFunction('totaldisplacement')

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(False, True)

# set scalar coloring
ColorBy(outputexoDisplay, ('POINTS', 'total displacement ', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
outputexoDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(totaldisplacementLUT, outputexoDisplay)

# current camera placement for renderView1
renderView1.CameraPosition = [1.4341019578383978, -1.5851958041371392, 0.8355853445366386]
renderView1.CameraFocalPoint = [0.027099601282502148, -0.03089584843385558, -0.09279653219987445]
renderView1.CameraViewUp = [-0.29998977152215256, 0.27418545604414307, 0.9136894837284449]
renderView1.CameraParallelScale = 0.7180703308172536

# save screenshot
SaveScreenshot('2LayerNormal_solution.png', renderView1, ImageResolution=[1225, 800])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [1.4341019578383978, -1.5851958041371392, 0.8355853445366386]
renderView1.CameraFocalPoint = [0.027099601282502148, -0.03089584843385558, -0.09279653219987445]
renderView1.CameraViewUp = [-0.29998977152215256, 0.27418545604414307, 0.9136894837284449]
renderView1.CameraParallelScale = 0.7180703308172536

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
