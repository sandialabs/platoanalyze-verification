import line
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-5
print "#L2_error_norm_tolerance:", tolerance


l = 5.0    ## length
E = 1.0e9  ## Young's modulus
g = 9.81   ## Acceleration due to gravity (m/s2)
p = 2700.0 ## mass density (kg/m3)


variable = {'type': 'vector', 'dim': 3, 'name': 'Displacements'}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-2.5, 0, 0], [2.5, 0, 0], variable)


# sample analytical solution
a_data = [g*p/E*(l*x_data[i]-x_data[i]*x_data[i]/2.0) for i in range(len(x_data))]

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
