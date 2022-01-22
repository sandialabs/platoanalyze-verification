import line
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-2
print "#L2_error_norm_tolerance:", tolerance


l = 0.25  ## layer thickness
e = 0.01  ## inherent strain


variable = {'type': 'vector', 'dim': 3, 'component': 2, 'name': 'total displacement', 'time': 3.0}

# get x, y data from results
z_data, disp_data = line.getLineData('./output_data/steps.pvd', [0, 0, -0.25], [0, 0, 0.75], variable)


# sample analytical solution
a_data = [0.0 for i in range(len(z_data))]
for i in range(len(z_data)):
  z = z_data[i]
  if z > 0 and z <= l:
    a_data[i] = -z*e*l
  elif z > l and z <= 2.0*l:
    a_data[i] = (1.0-l)*e*z - e*l
  elif z > 2.0*l and z <= 3.0*l:
    a_data[i] = (1.0-l)*e*z - 2.0*e*l
  elif z > 3.0*l and z <= 4.0*l:
    a_data[i] = (1.0-l)*e*z - 3.0*e*l

# compute error norm
error_norm = 0.0
for i in range(len(z_data)):
  error_norm += (disp_data[i]-a_data[i])*(disp_data[i]-a_data[i])

# OBLIGATORY:  the test harness looks for '#L2_error_norm_value' 
error_norm = math.sqrt(error_norm)
print "#L2_error_norm_value: ", error_norm

print "#X, computed, analytical"
for i in range(len(z_data)):
  print z_data[i], disp_data[i], a_data[i]
