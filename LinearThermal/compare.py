import line
import math

l = 2.0    ## length
k = 1.0e3  ## thermal conductivity
q = 1.0    ## flux boundary condition
T = 0.0    ## fixed temperature BC


# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-1, 0, 0], [1, 0, 0], 'Temperature')


# sample analytical solution
a_data = [T + q/k*(l - x_data[i]) for i in range(len(x_data))]

# compute error norm
error_norm = 0.0
for i in range(len(x_data)):
  error_norm += (y_data[i]-a_data[i])*(y_data[i]-a_data[i])

error_norm = math.sqrt(error_norm)
print "#L2_norm_of_error: ", error_norm

print "#X, computed, analytical"
for i in range(len(x_data)):
  print x_data[i], y_data[i], a_data[i]
