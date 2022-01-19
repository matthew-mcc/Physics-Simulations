import numpy as np
import math
import matplotlib.pylab as plt

#part a
def linear_model(x, param):
    #for input slope and intercept return $y = m x + b$
    
    slope, intercept = param
    result = slope*x + intercept
    return result

#part b
slope0, intercept0 = 1.2, 0.5
###y_model = linear_model(x, (slope0, intercept0))

#part c

data_points = np.loadtxt("C:\GIT\PHYS381\PHYS381_Assign5\data_points_assign5.txt")
control_variable_x = data_points[:,0]
measured_quality_y = data_points[:,1]

#part d
x = control_variable_x
y = linear_model(x, (slope0, intercept0))

plt.plot(control_variable_x, measured_quality_y, 'ro', label="Raw Text File")
plt.plot(x, y, 'b', label="Linear Model")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

#equation 9 first
#x2n = x^2 / N

def x2n_first(data):
    return data / data.size

#equation 10 fxn
def x2n(expected, observed, uncertainty=1):
    temp = ((expected - observed)/uncertainty) **2
    return sum(temp)


#part e
incercept_sequence = np.linspace(0.0, 3.0, 101)
slope_sequence = np.linspace(0.0, 1.0, 101)