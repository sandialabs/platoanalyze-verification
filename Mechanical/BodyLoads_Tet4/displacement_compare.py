import line
import verification_utils
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=1e-5)


l = 5.0    ## length
E = 1.0e9  ## Young's modulus
g = 9.81   ## Acceleration due to gravity (m/s2)
p = 2700.0 ## mass density (kg/m3)


variable = {'type': 'vector', 'dim': 3, 'name': 'displacement '}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data.exo', [-2.5, 0, 0], [2.5, 0, 0], variable)


# sample analytical solution
a_data = [g*p/E*(l*x_data[i]-x_data[i]*x_data[i]/2.0) for i in range(len(x_data))]

verification_utils.computeAndPrintErrorNorm(y_data, a_data)
verification_utils.printLineSolution(x_data, y_data, a_data)