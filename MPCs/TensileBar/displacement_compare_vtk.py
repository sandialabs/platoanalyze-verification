import line
import verification_utils
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=1e-5)

A = 1.0     ## area
E = 1.0e8   ## Young's modulus
F = 4.0e3   ## applied force (N)


variable = {'type': 'scalar', 'dim': 1, 'name': 'displacement X'}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-1.5, 0, 0], [3.5, 0, 0], variable)

# sample analytical solution
a_data = [F/E/A*(x_data[i]) for i in range(len(x_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(y_data, a_data)
verification_utils.printLineSolution(x_data, y_data, a_data)
