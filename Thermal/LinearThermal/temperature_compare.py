import verification_utils
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=1e-8)

l = 2.0    ## length
k = 1.0e3  ## thermal conductivity
q = 1.0    ## flux boundary condition
T = 0.0    ## fixed temperature BC

variable = {'name': 'temperature'}

# get x, y data from results
x_data, y_data = verification_utils.getLineData('./output_data.exo', variable, 'plot')

# sample analytical solution
a_data = [T - q/k*(l - x_data[i]) for i in range(len(x_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(y_data, a_data)
verification_utils.printLineSolution(x_data, y_data, a_data)
