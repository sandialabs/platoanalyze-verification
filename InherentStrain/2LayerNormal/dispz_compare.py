import verification_utils
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=1e-9)


l = 0.125  ## layer thickness
e = -0.01  ## inherent strain


variable = {'name': 'total displacement Z', 'time': 1.0}

# get x, y data from results
z_data, disp_data = verification_utils.getLineData('./output_data.exo', variable, 'plot')

# sample analytical solution
uc = -l*l/(2.0*l)*e
a_data = [(z_data[i]*uc/l if z_data[i] < l else 2.0*uc-z_data[i]*uc/l) for i in range(len(z_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(disp_data, a_data)

verification_utils.printLineSolution(z_data, disp_data, a_data)
