import line
import math

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-9
print "#L2_error_norm_tolerance:", tolerance


l = 0.125  ## layer thickness
e = -0.01  ## inherent strain


variable = {'type': 'vector', 'dim': 3, 'component': 2, 'name': 'total displacement', 'time': 1.0}

# get x, y data from results
z_data, disp_data = line.getLineData('./output_data/steps.pvd', [0, 0, -0.125], [0, 0, 0.125], variable)


# sample analytical solution
uc = -l*l/(2.0*l)*e
a_data = [(z_data[i]*uc/l if z_data[i] < l else 2.0*uc-z_data[i]*uc/l) for i in range(len(z_data))]

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
