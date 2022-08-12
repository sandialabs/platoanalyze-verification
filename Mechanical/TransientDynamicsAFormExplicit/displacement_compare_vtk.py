import line
import verification_utils
import math

def displacement(x):
  t = 2.0e-7
  return 0.001*math.sin(3.14159264*(x-501840.435*t))



# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=1e-3)

variable = {'type': 'scalar', 'dim': 1, 'name': 'displacement X', 'time': 27.0}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-0.5, 0, 0], [0.5, 0, 0], variable)


# sample analytical displacement solution
a_data = [displacement(-0.5+x_data[i]) for i in range(len(x_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(y_data, a_data)
verification_utils.printLineSolution(x_data, y_data, a_data)