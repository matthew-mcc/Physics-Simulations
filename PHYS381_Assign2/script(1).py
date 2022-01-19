#Assignment 2: The Pendulum Problem
#Exercise4 Python script to solve the linear pendulum equation
#Importing the libraries that are going to be used
import matplotlib.pylab as plt
import numpy as np
import math
#defining the variables and parameters that will be used throughout the assignment
#g is the gravitational constant, L is the length of the pendulum system
#k is the dampening constant, A is the amplitude and phi is the angular frequency
g = 9.81
L = 1.0
k = 0.0 #value for first exercise
A = 0.0 #value for first exercise
phi = 0.66667 #value for first exercise

#defining a function based upon equation 11
#assuming that sin theta is approximately equal to theta for the linear model
def f(theta, w, t):
  #this function will be used to model the pendulum system. 
  return ((-g/L) * math.sin(theta) - k * w) + (A * math.cos(phi * t))
  

#setting initial values for the variables that f calls upon
#dt is delta t, the increments of change that t will go through
theta = 0.2
w = 0.0
t = 0.0
dt = 0.01

#Adding the code for the trapezoid rule equations from the assignment 2 outline
#this comes from equations 21 and 22
#the total number of steps taken will be 1000 in this case
t_list = [0.0]
thet_list =  [0.0]
w_list = [0.0]
for steps in range (1, 1000):
  k1a = dt * w
  k1b = dt * f(theta, w, t) # This line doesn't work #Works now!
  k2a = dt * (w + k1b)
  k2b = dt * f(theta + k1a, w + k1b, t + dt)
  theta = theta + (k1a + k2a)/2
  w = w + (k1b + k2b)/2
  t = t + dt
  t_list.append(t)
  thet_list.append(theta)
  w_list.append(w)

#first plot
plt.plot(t_list, thet_list)                       
plt.plot(t_list, w_list)
plt.ylim(-math.pi, math.pi)                            
plt.show()         
#second plot
t_list[0] = 0.0
thet_list[0] = 1.0
w_list[0] = 0.0  
plt.plot(t_list, thet_list)                       
plt.plot(t_list, w_list)
plt.ylim(-math.pi, math.pi)                            
plt.show()
#third plot
t_list[0] = 0.0
thet_list[0] = 3.1
w_list[0] = 0.0  
plt.plot(t_list, thet_list)                       
plt.plot(t_list, w_list)
plt.ylim(-math.pi, math.pi)                            
plt.show()       
#fourth plot
t_list[0] = 0.0
thet_list[0] = 0.0
w_list[0] = 1.0 
plt.plot(t_list, thet_list)                       
plt.plot(t_list, w_list)
plt.ylim(-math.pi, math.pi)                            
plt.show()            