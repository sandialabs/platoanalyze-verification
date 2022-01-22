import line
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-5
print "#L2_error_norm_tolerance:", tolerance


A = 1.0     ## area
E = 1.0e8   ## Young's modulus
F = 4.0e3   ## applied force (N)


variable = {'type': 'vector', 'dim': 3, 'name': 'displacement '}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data.exo', [-1.5, 0, 0], [3.5, 0, 0], variable)

# sample analytical solution
a_data = [F/E/A*(x_data[i]) for i in range(len(x_data))]

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
