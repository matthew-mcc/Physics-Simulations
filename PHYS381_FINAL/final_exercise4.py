#imports
import matplotlib.pyplot as plt
import numpy as np
import math

#reading in text file, then plotting
signal = np.loadtxt("superposition_signal.txt", float)
plt.figure()
plt.plot(signal)
plt.xlabel("time")
plt.ylabel("signal")
plt.grid()
plt.show()

#Constants and lists that will be used 
N = 128
h = 0.1 
t = 0 
dt = 0.001
tau = N * h
y_list = []
t_list = []

#setting v1,v2,v3 values from the power spectrum
v1, v2, v3 = 439, 219, 110

#Orignal function that we will try to reconstruct
while t <= tau:
    #equation 6 calculation
  y = (1/3)*(math.cos(2*math.pi*t*v1) + math.cos(2*math.pi*t*v2) + math.cos(2*math.pi*t*v3))

  t = t + dt #iterating t

  y_list.append(y) #appending y list

  t_list.append (t) #appending t list


#First graph - Plot original function 
plt.plot(t_list,y_list) 
plt.xlabel("Time step (arbitrary)")
plt.ylabel("Amplitude (unitless)")
plt.grid()
plt.show()


N = len(signal) #length of your timeline is now length of signal

#real and imaginary lists
re_list = []
im_list = []

#nested for loop to obtain real and imaginary components
for n in range(N):
    re = 0
    im = 0
    for m in range(N):
        re = re + signal[m] * math.cos(2*math.pi*m*n/float(N)) #getting real
        im = im + signal[m] * math.sin(2*math.pi*m*n/float(N)) #getting imaginary

    re_list.append(re) #appending real
    im_list.append(im) #appending imaginary

#plotting power spectrum   
plt.figure() 
plt.plot(np.sqrt(np.asarray(re_list)**2 + np.asarray(im_list)**2))
plt.xlabel('component index')
plt.ylabel('Power spectrum')
plt.grid()
plt.show()

