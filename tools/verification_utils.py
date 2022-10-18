import math
import exodus

def printErrorTolerance(tol: float) -> None:
    """
    Prints a tolerance using the format expected by the test harness
    """
    print(f"#L2_error_norm_tolerance: {tol}")

def computeAndPrintErrorNorm(computed_data: list, baseline_data: list) -> None:
    """
    Computes the L2 norm of the difference of computed_data and baseline_data and
    prints the result using the format expected by the test harness
    """
    error_norm = sum((x - y)**2 for x, y in zip(computed_data, baseline_data))
    error_norm = math.sqrt(error_norm)
    print(f"#L2_error_norm_value: {error_norm}")

def printLineSolution(x_data: list, computed_y_data: list, baseline_y_data) -> None:
    """
    Prints a solution computed along a line, including the position on the line and
    both the computed band baseline solution values.
    """
    print("#X, computed, analytical")
    for x, computed, baseline in zip(x_data, computed_y_data, baseline_y_data):
        print(x, computed, baseline)

def getLineData(fileName: str, variable: tuple, nodeset: str) -> (list,list):
    """
    Returns the x,y data for 'variable' from mesh 'filename' on 'nodeset'.
    """
    cDimension = 3;

    inMesh = exodus.ExodusDB()
    inMesh.read(fileName)

    tNodes = []
    tFound = False
    for tNodeSet in inMesh.NodeSets:
      if tNodeSet.name == nodeset:
        tNodes = tNodeSet.nodes
        tFound = True

    if tFound == False:
     raise Exception("Node set '" + nodeset + "' not found")

    if len(tNodes) == 0:
     raise Exception("Found empty node set")

    tSearchNodes = [tNode for tNode in tNodes]
    tSearchX = [inMesh.getCoordData(tNode,"index") for tNode in tNodes]

    #### find bounding box
    tBoxLimitVals = [[1e12,-1e12],[1e12,-1e12],[1e12,-1e12]]
    tBoxLimitInds = [[0,0],[0,0],[0,0]]
    for iNode, X in enumerate(tSearchX):
      for iDim in range(cDimension):
        if X[iDim] < tBoxLimitVals[iDim][0]:
          tBoxLimitVals[iDim][0] = X[iDim]
          tBoxLimitInds[iDim][0] = iNode
        if X[iDim] > tBoxLimitVals[iDim][1]:
          tBoxLimitVals[iDim][1] = X[iDim]
          tBoxLimitInds[iDim][1] = iNode

    #### find widest range
    tSortDim = 0
    tSortWidth = 0.0
    for iDim in range(cDimension):
      if tBoxLimitVals[iDim][1] - tBoxLimitVals[iDim][0] > tSortWidth:
        tSortDim = iDim
        tSortWidth = tBoxLimitVals[iDim][1] - tBoxLimitVals[iDim][0]

    #### sort nodes
    tSortedNodes = [tSearchNodes.pop(tBoxLimitInds[tSortDim][0])]
    tSortedPos = [tSearchX.pop(tBoxLimitInds[tSortDim][0])]

    tNumSearch = len(tSearchNodes)
    for tIndex in range(tNumSearch):
      tClosestNode = 0
      tClosestDist = 1e12
      for tLocalIndex, tGlobalIndex in enumerate(tSearchNodes):
        if tSearchX[tLocalIndex][tSortDim] - tSortedPos[-1][tSortDim] < tClosestDist:
          tClosestNode = tLocalIndex
          tClosestDist = tSearchX[tLocalIndex][tSortDim] - tSortedPos[-1][tSortDim]
      tSortedNodes.append(tSearchNodes.pop(tClosestNode))
      tSortedPos.append(tSearchX.pop(tClosestNode))

    variableName = variable['name']
    variableTime = variable.get('time', 0.0)

    tTimeIndex = 0
    tTimeValue = 0.0
    for tIndex, tTime in enumerate(inMesh.varTimes):
      if math.fabs(variableTime - tTime) < math.fabs(variableTime - tTimeValue):
        tTimeIndex = tIndex

    tVariableData = []
    for tIndex, tName in enumerate(inMesh.nodeVarNames):
      if tName == variableName:
        tVariableData = inMesh.nodeVars[tTimeIndex][tIndex]

    if len(tVariableData) == 0:
      raise Exception("Requested variable ('" + variableName + "') not found")

    tSortedX = []
    for X in tSortedPos:
      tDist = 0.0
      for iDim in range(cDimension):
        tDist += (X[iDim]-tSortedPos[0][iDim])*(X[iDim]-tSortedPos[0][iDim])
      tSortedX.append(math.sqrt(tDist))

    tSortedY = [tVariableData[tNode] for tNode in tSortedNodes]

    return tSortedX, tSortedY

