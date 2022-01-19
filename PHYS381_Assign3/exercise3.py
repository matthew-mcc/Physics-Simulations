import numpy as np
import matplotlib.pylab as plt

#Parameters
M = 1.0
g = 9.8
V = 80
ang = 60.0
b = 0.004
dt = 0.5

#lists
t = [0]
vx = [V * np.cos(ang/180*np.pi)]
vy = [V * np.sin(ang/180*np.pi)]
x = [0]
y = [0]


drag = b * V #quad !


#accelerations
ax = [-(drag*np.cos(ang/180*np.pi))/M]
ay = [-g-(drag*np.sin(ang/180*np.pi))/M]

dt = 0.25
#using euler method

count = 0
while y[count] >= 0: #itterating 10 tinems
    t.append(t[count] + dt)

    vx.append(vx[count] + dt*ax[count])
    vy.append(vy[count] + dt*ay[count])

    x.append(x[count]+dt*vx[count])
    y.append(y[count]+dt*vy[count])

    vel = np.sqrt(vx[count+1]**2 + vy[count+1]**2)
    drag = b * vel 
    ax.append(-(drag*np.cos(ang/180*np.pi))/M)
    ay.append(-g-(drag*np.sin(ang/180*np.pi))/M)
    count += 1


plt.plot(x,y, 'bo')
plt.ylabel("Y(m)")
plt.xlabel("X(m)")
plt.show()
