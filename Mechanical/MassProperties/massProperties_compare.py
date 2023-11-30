import exodus
import PlatoPython
import numpy as np

# boilerplate that dynamically loads the mpi library required by PlatoPython.Analyze
import ctypes
ctypes.CDLL("libmpi.so",mode=ctypes.RTLD_GLOBAL)

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-2
print("#L2_error_norm_tolerance:", tolerance)

# Cylinder properties for analytic solutions
height = 5.0
radius = 1.5
density = 1.0
offsetX = 2.0
offsetY = 5.0
offsetZ = 3.0

# get mesh
outMesh = exodus.ExodusDB()
outMesh.read("cylinder.exo");
numNodes = outMesh.numNodes;
outMesh.read("cylinder_shifted.exo");
numNodesShifted = outMesh.numNodes;

# Mass
analyze = PlatoPython.Analyze("analyzeInputMass.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldMass = height*np.pi*radius*radius
computedMass = np.sqrt(objective)
errorMass = np.abs(computedMass - goldMass) / goldMass
print("\n Mass:")
print("Gold: ", goldMass)
print("Computed: ", computedMass)
print("Error: ", errorMass)
print("\n")

# Ixx
analyze = PlatoPython.Analyze("analyzeInputIxx.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldIxx = goldMass*(3.0*radius*radius + height*height) / 12.0
computedIxx = np.sqrt(objective)
errorIxx = np.abs(computedIxx - goldIxx) / goldIxx
print("\n Ixx:")
print("Gold: ", goldIxx)
print("Computed: ", computedIxx)
print("Error: ", errorIxx)
print("\n")

# Iyy
analyze = PlatoPython.Analyze("analyzeInputIyy.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldIyy = goldMass*(3.0*radius*radius + height*height) / 12.0
computedIyy = np.sqrt(objective)
errorIyy = np.abs(computedIyy - goldIyy) / goldIyy
print("\n Iyy:")
print("Gold: ", goldIyy)
print("Computed: ", computedIyy)
print("Error: ", errorIyy)
print("\n")

# Izz
analyze = PlatoPython.Analyze("analyzeInputIzz.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldIzz = goldMass*radius*radius / 2.0
computedIzz = np.sqrt(objective)
errorIzz = np.abs(computedIzz - goldIzz) / goldIzz
print("\n Izz:")
print("Gold: ", goldIzz)
print("Computed: ", computedIzz)
print("Error: ", errorIzz)
print("\n")

# Ixy
analyze = PlatoPython.Analyze("analyzeInputIxy.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldIxy = 0.0
computedIxy = np.sqrt(objective)
errorIxy = np.abs(computedIxy)
print("\n Ixy:")
print("Gold: ", goldIxy)
print("Computed: ", computedIxy)
print("Error: ", errorIxy)
print("\n")

# Ixz
analyze = PlatoPython.Analyze("analyzeInputIxz.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldIxz = 0.0
computedIxz = np.sqrt(objective)
errorIxz = np.abs(computedIxz)
print("\n Ixz:")
print("Gold: ", goldIxz)
print("Computed: ", computedIxz)
print("Error: ", errorIxz)
print("\n")

# Iyz
analyze = PlatoPython.Analyze("analyzeInputIyz.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodes)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldIyz = 0.0
computedIyz = np.sqrt(objective)
errorIyz = np.abs(computedIyz)
print("\n Iyz:")
print("Gold: ", goldIyz)
print("Computed: ", computedIyz)
print("Error: ", errorIyz)
print("\n")

# CGx
analyze = PlatoPython.Analyze("analyzeInputCGx.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodesShifted)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldCGx = offsetX
computedCGx = np.sqrt(objective)
errorCGx = np.abs(computedCGx - goldCGx) / goldCGx
print("\n CGx:")
print("Gold: ", goldCGx)
print("Computed: ", computedCGx)
print("Error: ", errorCGx)
print("\n")

# CGy
analyze = PlatoPython.Analyze("analyzeInputCGy.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodesShifted)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldCGy = offsetY
computedCGy = np.sqrt(objective)
errorCGy = np.abs(computedCGy - goldCGy) / goldCGy
print("\n CGy:")
print("Gold: ", goldCGy)
print("Computed: ", computedCGy)
print("Error: ", errorCGy)
print("\n")

# CGz
analyze = PlatoPython.Analyze("analyzeInputCGz.xml", "analyzeOperations.xml", "Mass")
analyze.initialize();
vals = [1.0 for i in range(numNodesShifted)];
analyze.importData("Topology", "SCALAR_FIELD", vals)
analyze.compute("Compute Criterion Value")
objective = analyze.exportData("Objective Value", "SCALAR")
analyze.finalize()

goldCGz = offsetZ
computedCGz = np.sqrt(objective)
errorCGz = np.abs(computedCGz - goldCGz) / goldCGz
print("\n CGz:")
print("Gold: ", goldCGz)
print("Computed: ", computedCGz)
print("Error: ", errorCGz)
print("\n")

# Max error
maxError = np.max(np.array([errorMass, errorIxx, errorIyy, errorIzz, errorIxy, errorIxz, errorIyz, errorCGx, errorCGy, errorCGz]))

# OBLIGATORY:  the test harness looks for '#L2_error_norm_value' 
print("#L2_error_norm_value: ", maxError)

