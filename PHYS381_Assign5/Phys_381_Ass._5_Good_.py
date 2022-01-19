#!/usr/bin/env python
# coding: utf-8

# In[8]:


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

#part c
data_points = np.loadtxt("data_points_assign5.txt")
control_variable_x = data_points[:,0]
measured_quality_y = data_points[:,1]

y_data = np.asarray(measured_quality_y)
x_data = np.asarray(control_variable_x)

#part d
x = control_variable_x
y = linear_model(x_data, (slope0, intercept0))

plt.figure(0)
plt.title("Figure 1: First linear model fit with data points")
plt.plot(control_variable_x, measured_quality_y, 'ro', label="Raw Text File")
plt.plot(x, y, 'b', label="Linear Model")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show() 

def x2n_first(data):
    return data / data.size

#equation 10 fxn
def x2n(expected, observed, uncertainty=1):
    temp = ((observed - expected)/uncertainty) 
    return sum(temp**2) / len(expected)

result = x2n(measured_quality_y,y)
print("The calculate chi Squared value for this model (figure 1) is:", result)

#The fitting model at this stage is okay but could be a lot better. We see that at the start of the data points 
#the model follows well, stikcing to the lower values for its curve. At larger x and y values, the model 
#begins to fail as it no longer follows the desired trend and veers off. This is exemplified by calculating the chi
#squared value to be 2.507, which is large and can be reduced for a better model. 


intercept_sequence = np.linspace(0.0, 3.0, 101)
slope_sequence = np.linspace(0.0, 3.0, 101)

rchi2 = np.zeros([len(intercept_sequence),len(slope_sequence)])


for n,i in enumerate(intercept_sequence):
    
    for k,j in enumerate(slope_sequence):
        opt = linear_model(x_data, (j,i))
    
    
        rchi2[k,n]= x2n(opt,y_data)
    
xmin = np.argmin(rchi2)
(row,col)= np.unravel_index(xmin,rchi2.shape)


print("Re-caluclting using a matrix function, the row and column for the smallest rchi2 value is:", row,col)
print("Which correlates to a new rchi^2 value of:", rchi2[49,12])

print("Where intercept sequence value is :", intercept_sequence[12])
print("and the slope sequence value is:", slope_sequence[49])

test_var = rchi2[range(len(intercept_sequence)),k]
test_var_2 = rchi2[row,range(len(slope_sequence))]
min_val = 100
min_index = 0
for i in range(test_var.size):
    if test_var[i] < min_val:
        min_val = test_var[i]
        min_index = i
    else:
        i= i+1

min_val_2 = 100
min_index_2 = 0
for i in range(test_var_2.size):
    if test_var_2[i] < min_val_2:
        min_val_2 = test_var_2[i]
        min_index_2 = i
    else:
        i = i + 1



print('index', min_index, 'val',min_val)
print(intercept_sequence[min_index])

plt.figure(1)
plt.title("Figure 2: Slope and intercept Sequences as a function of rchi^2")
plt.plot(intercept_sequence, test_var)
plt.plot(intercept_sequence[min_index], min_val, 'ro')
plt.plot(slope_sequence, test_var_2)
plt.plot(slope_sequence[min_index_2], min_val_2, 'bo')
plt.xlabel("Slope/intercept sequence")
plt.ylabel("rchi^2")
plt.grid()
plt.show()


xx, yy = np.meshgrid(slope_sequence, intercept_sequence)

plt.figure(3)
plt.title("Figure 3: 3D relationship between slope, intercept, and rchi^2")
plt.contour(xx, yy, rchi2, 70)
plt.xlabel("slope sequence")
plt.ylabel("intercept sequence")
plt.show()

# Talk about each figure, the numbers found, what they represent. 
# Figure 1 - 
# Figure 2 - 
# Figure 3 - 

# In[4]:


#PART 2 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

data_points = open('data_points_assign5.txt', 'r') #np.loadtxt("data_points_assign5.txt")
data = data_points.readlines()
data_points.close()

xvalues = [] #data_points[:,0]
yvalues = [] #data_points[:,1]


#for loop 
for i in data:
    col = i.split()
    xvalues.append(float(col[0]))
    
    yvalues.append(float(col[1]))
    

xarray = np.asarray(xvalues)
yarray = np.asarray(yvalues)


guess = [1.2, 0.5]
slope0, intercept0 = guess 

#Has to be changed 
def linear_model(x, param):
    #for input slope and intercept return $y = m x + b$

    slope, intercept = param
    result = slope*x + intercept
    return result

#function for y = linear_model(x, (slope0, intercept0)) - need to pass xdata points through. Then pass to min fn 

#x = xvalues
y = linear_model(xvalues, (slope0, intercept0))

#first arg is y 
mins = minimize(y, guess, (xvalues, yvalues), method = 'Nelder-Mead')
print(yvalues)


# plt.plot(x, y)
# plt.plot(x, yvalues, 'ro')
# plt.show()


# 
