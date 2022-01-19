#2A
import matplotlib.pylab as plt
import math
import numpy as np

#First bullet point - plot the function f(t) = sin(0.45*t*pi), incrementing until tau = Nh 
N = 128
h = 0.1 


t = 0 
dt = 0.001
tau = N * h
y_list = []
t_list = []

while t <= tau:
  y = math.sin(0.45*math.pi*t)

  t = t + dt 

  y_list.append(y)

  t_list.append (t)



plt.plot(t_list,y_list) 
plt.xlabel("Time (sec)")
plt.ylabel("Displacement (m)")
plt.grid()
plt.show()

t_list = []
re_list = []
im_list = []


pi2 = math.pi * 2
for n in range(N):
  re = 0
  im = 0

  temp = n * h
  t_list.append(temp)
  for m in range(N):
    re = re + math.sin(0.45*math.pi*m*h) * math.cos(2*math.pi*m*n/N)
    im = im + math.sin(0.45*math.pi*m*h) * math.sin(2*math.pi*m*n/N)
  re_list.append(re)
  im_list.append(im)

plt.plot(t_list, re_list)
plt.show()

#reconstruction thing 
t_list1 = []
fm_list = []
for n in range(N):
  fm = 0 
  temp = n * h
  t_list1.append(temp)
  for m in range(N):
    fm = fm + ((re_list[n]*math.cos(2*math.pi*m*n/N)) + (im_list[n]*math.sin(2*math.pi*m*n/N)))
  fm_list.append(fm)
  print(fm)
plt.plot(t_list1, fm_list)
plt.show()