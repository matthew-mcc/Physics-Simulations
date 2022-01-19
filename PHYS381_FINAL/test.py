import numpy as np
import matplotlib.pyplot as plt
import math

#Constants and lists that will be used 
N = 128
h = 0.1 
t = 0 
dt = 0.001
tau = N * h
y_list = []
t_list = []
v1, v2, v3 = 439, 219, 110

#Orignal function that we will try to reconstruct
while t <= tau:
  y = (1/3)*(math.cos(2*math.pi*t*v1) + math.cos(2*math.pi*t*v2) + math.cos(2*math.pi*t*v3))

  t = t + dt 

  y_list.append(y)

  t_list.append (t)


#First graph - Plot original function 
plt.plot(t_list,y_list) 
plt.xlabel("Time step (arbitrary)")
plt.ylabel("Amplitude (unitless)")
plt.grid()
plt.show()