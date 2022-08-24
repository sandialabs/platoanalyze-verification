#### import the simple module from the paraview
from paraview.simple import *

def getLineData(fileName, x0, x1, variable):

  variableName = variable['name']
  variableDim  = variable.get('dim', 3)
  variableType = variable.get('type', 'scalar')
  variableTime = variable.get('time', 0.0)
  variableComp = variable.get('component', 0)

  # create a new 'PVD Reader'
  stepspvd = PVDReader(FileName=fileName)

  # create a new 'Plot Over Line'
  plotOverLine1 = PlotOverLine(Input=stepspvd, Source='Line')

  # Properties modified on plotOverLine1
  plotOverLine1.Tolerance = 2.22044604925031e-16

  # set time
  plotOverLine1.UpdatePipeline(variableTime)

  # Properties modified on plotOverLine1.Source
  plotOverLine1.Source.Point1 = x0
  plotOverLine1.Source.Point2 = x1

  fetchData = paraview.servermanager.Fetch(plotOverLine1)
  pointData = fetchData.GetPointData()
  fieldData = pointData.GetArray(variableName)
  posData = pointData.GetArray('arc_length')
  x_Data = [posData.GetValue(i) for i in range(posData.GetSize())]

  y_Data = []
  if variableType == 'scalar':
    y_Data = [fieldData.GetValue(i) for i in range(fieldData.GetSize())]
  elif variableType == 'vector':
    numEntries = int(fieldData.GetSize()/variableDim)
    y_Data = [fieldData.GetValue(i*variableDim+variableComp) for i in range(numEntries)]

  return x_Data, y_Data

