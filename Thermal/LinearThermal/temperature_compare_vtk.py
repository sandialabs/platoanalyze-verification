import line
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-8
print "#L2_error_norm_tolerance:", tolerance


l = 2.0    ## length
k = 1.0e3  ## thermal conductivity
q = 1.0    ## flux boundary condition
T = 0.0    ## fixed temperature BC


variable = {'name': 'temperature'}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-1, 0, 0], [1, 0, 0], variable)


# sample analytical solution
a_data = [T - q/k*(l - x_data[i]) for i in range(len(x_data))]

# compute error norm
error_norm = 0.0
for i in range(len(x_data)):
  error_norm += (y_data[i]-a_data[i])*(y_data[i]-a_data[i])

# OBLIGATORY:  the test harness looks for '#L2_error_norm_value' 
error_norm = math.sqrt(error_norm)
print "#L2_error_norm_value: ", error_norm

print "#X, computed, analytical"
for i in range(len(x_data)):
  print x_data[i], y_data[i], a_data[i]
