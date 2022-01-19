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