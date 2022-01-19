import numpy as np
import matplotlib.pyplot as plt
import math

#masses obtained from jupyter ex3
#seed = 2319804890
Mr = 4116 #Mass of Rocket without Fuel
Mf = 8909 #Mass of Fuel
Mt = 13025 #Total Mass of Rocket with Fuel

#The rocket consumes fuel at a rate of 129.4kg/s
#Fnet = Fthrust - Fg - Fdrag
#Fg = Mg
#Fdrag = 0.5 * P * V^2 * C * A
#Fthrust = Ve * dm/dt

#Define Parameters 
g = 9.81
fuel_rate = 124.9
P = 1.22
C = 0.125

#area calculation
D = 1.65
r = D/2
A = math.pi * r*r
print(A)
Ve = 2050
#We need to use Euler numerical Integration to solve, considering two stages
#Stage1 = Ascending while it has fuel with its total mass M reducing with time
#Stage2 = Descending once all of its fuel has been burnt and its mass is constant
#Need 4 plots, V vs T and H vs T for both stages

#Start with stage 1
#need to define lists

dt = 0.1
h = 0
V = 2050
t = 0.0
tt = [t]
hh = [h]
vv = [V]
aa = [0]
Mtot = Mf + Mr
dm = 0
sign = 1
while h >= 0: #while the rocket is above ground
    
    if dm > 8909:
        dm = 0 
    if V < 0:
        sign = -1
    
    dm = fuel_rate * t
    Fdrag = sign* 0.5 * P * C * A * V**2
    Fgravity = 9.8 * Mtot
    Fthrust = (2050) * (dm/dt)
    Net_Force = Fthrust - Fgravity
    acceleration = (Net_Force / Mt) 
    V = V + acceleration * dt
   
    h = h + V * dt
    Mt = Mt - dm
    t = t + dt
    tt.append(t)
    hh.append(h)
    vv.append(V)
plt.plot(tt, vv, 'r')
plt.title("Velocity vs Time")
plt.show()
plt.plot(tt, hh, 'b')
plt.title("Altitude vs Time")
plt.show()





