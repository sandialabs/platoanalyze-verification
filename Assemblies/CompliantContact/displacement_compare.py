import verification_utils
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=3e-4)

A = 1.0     ## area
E = 1.0e8   ## Young's modulus
F = 4.0e3   ## applied force (N)

variable = {'name': 'displacement X'}

# get x, y data from results
x_data, y_data = verification_utils.getLineData('./output_data.exo', variable, 'plot')

# sample analytical solution
a_data = [F/E/A*(x_data[i]) for i in range(len(x_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(y_data, a_data)
verification_utils.printLineSolution(x_data, y_data, a_data)
