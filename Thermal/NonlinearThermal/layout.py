#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'ExodusIIReader'
blockexo = ExodusIIReader(FileName=['./block.exo'])
blockexo.SideSetArrayStatus = []

# Properties modified on blockexo
blockexo.SideSetArrayStatus = ['x0', 'x1']
blockexo.ElementBlocks = ['Unnamed block ID: 1 Type: TETRA']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [684, 667]

# show data in view
blockexoDisplay = Show(blockexo, renderView1)
# trace defaults for the display properties.
blockexoDisplay.Representation = 'Surface'
blockexoDisplay.ColorArrayName = [None, '']
blockexoDisplay.OSPRayScaleArray = 'GlobalNodeId'
blockexoDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
blockexoDisplay.SelectOrientationVectors = 'GlobalNodeId'
blockexoDisplay.ScaleFactor = 0.1
blockexoDisplay.SelectScaleArray = 'GlobalNodeId'
blockexoDisplay.GlyphType = 'Arrow'
blockexoDisplay.GlyphTableIndexArray = 'GlobalNodeId'
blockexoDisplay.DataAxesGrid = 'GridAxesRepresentation'
blockexoDisplay.PolarAxes = 'PolarAxesRepresentation'
blockexoDisplay.ScalarOpacityUnitDistance = 0.014462850878067382

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(blockexoDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
blockexoDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# hide color bar/color legend
blockexoDisplay.SetScalarBarVisibility(renderView1, False)

# create a new 'ExodusIIReader'
blockexo_1 = ExodusIIReader(FileName=['./block.exo'])
blockexo_1.SideSetArrayStatus = []

# Properties modified on blockexo_1
blockexo_1.ElementBlocks = ['Unnamed block ID: 1 Type: TETRA']

# show data in view
blockexo_1Display = Show(blockexo_1, renderView1)
# trace defaults for the display properties.
blockexo_1Display.Representation = 'Surface'
blockexo_1Display.ColorArrayName = [None, '']
blockexo_1Display.OSPRayScaleArray = 'GlobalNodeId'
blockexo_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
blockexo_1Display.SelectOrientationVectors = 'GlobalNodeId'
blockexo_1Display.ScaleFactor = 0.1
blockexo_1Display.SelectScaleArray = 'GlobalNodeId'
blockexo_1Display.GlyphType = 'Arrow'
blockexo_1Display.GlyphTableIndexArray = 'GlobalNodeId'
blockexo_1Display.DataAxesGrid = 'GridAxesRepresentation'
blockexo_1Display.PolarAxes = 'PolarAxesRepresentation'
blockexo_1Display.ScalarOpacityUnitDistance = 0.014486369191648989

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(blockexo_1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
blockexo_1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(blockexo)

# Properties modified on blockexo
blockexo.ElementBlocks = []

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(blockexo_1)

# change representation type
blockexo_1Display.SetRepresentationType('Wireframe')

# hide color bar/color legend
blockexo_1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [0.9049560841724831, 0.34743806530039345, 0.6086069361117896]
renderView1.CameraFocalPoint = [-0.5300349415808232, -0.42007141192824526, -0.5671246826873839]
renderView1.CameraViewUp = [-0.29630133181105356, 0.9240401231765312, -0.24156856485664113]
renderView1.CameraParallelScale = 0.5196152428442091

# save screenshot
SaveScreenshot('./NonlinearThermal_layout.png', renderView1, ImageResolution=[1267, 802])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.9049560841724831, 0.34743806530039345, 0.6086069361117896]
renderView1.CameraFocalPoint = [-0.5300349415808232, -0.42007141192824526, -0.5671246826873839]
renderView1.CameraViewUp = [-0.29630133181105356, 0.9240401231765312, -0.24156856485664113]
renderView1.CameraParallelScale = 0.5196152428442091

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
