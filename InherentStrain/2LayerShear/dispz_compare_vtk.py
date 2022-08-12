import line
import verification_utils
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
verification_utils.printErrorTolerance(tol=2e-2)

xdim = 1.0 ## x dimension (plot is along x)
ydim = 1.0 ## y dimension 
m = 1.0    ## thickness ratio (top layer thickness / bottom layer thickness)
n = 1.0    ## stiffness ratio (top layer stiffness / bottom layer stiffness)
t = 0.1    ## layer thickness (z)
e = 0.01   ## inherent strain

variable = {'type': 'vector', 'dim': 3, 'component': 2, 'name': 'total displacement', 'time': 1.0}

# get x, y data from results
x_data, disp_data = line.getLineData('./output_data/steps.pvd', [-0.5, 0.0, 0.0], [0.5, 0.0, 0.0], variable)

# sample analytical solution
k = (6.0*e*(1.0+m)*(1.0+m))/(t*(3.0*(1.0+m)*(1.0+m)+(1.0+m*n)*(m*m+1.0/(m*n))))
a_data = [(1.0-math.cos(x_data[i]*k))/k for i in range(len(x_data))]

# compute error norm
verification_utils.computeAndPrintErrorNorm(disp_data, a_data)
verification_utils.printLineSolution(x_data, disp_data, a_data)
