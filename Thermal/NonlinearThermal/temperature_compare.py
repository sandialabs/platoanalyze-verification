import line
import math

def sol(x):

  a0 = 205.0
  a1 = -0.02
  a2 = 0.0008

  T0 = 250.0
  T1 = 0.0

  c0 =  -math.pow(a1,3) + 6.0*a0*a1*a2 + 2.0*math.pow(a2,2)*T0*(6.0*a0 + T0*(3.0*a1 + 2.0*a2*T0))
  c1 = 2*math.pow(a2,2)*(-(T0*(6.0*a0 + T0*(3.0*a1 + 2.0*a2*T0))) + 6.0*a0*T1 + 3.0*a1*math.pow(T1,2) + 2.0*a2*math.pow(T1,3))
  c2 = math.sqrt(math.pow(-9.0*math.pow(a1,2) + 36.0*a0*a2,3) + 729.0*math.pow(math.pow(a1,3) \
     - 6.0*a1*a2*(a0 + a2*(-(math.pow(T0,2)*(-1 + x)) + math.pow(T1,2)*x)) \
     - 4.0*math.pow(a2,2)*(3.0*a0*(T0 - T0*x + T1*x) + a2*(-(math.pow(T0,3)*(-1.0 + x)) + math.pow(T1,3)*x)),2))/27.0

  return (-a1 + (math.pow(a1,2) - 4.0*a0*a2)/math.pow(c0 + c2 + c1*x,1.0/3.0) + math.pow(c0 + c2 + c1*x,1.0/3.0))/(2.*a2)


# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-1
print "#L2_error_norm_tolerance:", tolerance

l = 2.0    ## length
k = 1.0e3  ## thermal conductivity
q = 1.0    ## flux boundary condition
T = 0.0    ## fixed temperature BC


variable = {'name': 'Temperature'}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-1, 0, 0], [1, 0, 0], variable)


# sample analytical solution
a_data = [sol(x_data[i]) for i in range(len(x_data))]

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
