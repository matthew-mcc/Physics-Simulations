import matplotlib.pylab as plt
import numpy as np
import math


def vacuum():
    m, g, V, ang, dt = 1.0471975511965977e-09, 9.81, 2.3, 10.0, 0.0001
    t = 0
    vx = V * np.cos(ang/180*np.pi)
    vy = V * np.sin(ang/180*np.pi)
    x = 0
    y = 0 
    t_list = []
    x_list = []
    y_list = []

    while y >= 0:
        x = x + vx * t
        y = y + vy * t
        vy = vy - g * t
        t = t + dt
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list

def linear():
    # gravity acceleration
    g = 9.81 #m/s^2
    # diameter of the object
    D = 1.e-4 #m
    # volume of the object
    vol = (4.0/3.0) * math.pi * (D/2)**3
    # density (Kg/m^3)
    rho = 2000
    # mass of the object
    m = rho * vol
    
    # features of the drag force
    B = 1.6e-4
    b = B*D

    # time spacing
    dt = 0.001

    # angle of throw (in degree)
    theta = 10.0

    # degrees2radians
    theta_rads = math.radians(theta)

    # initial conditions (with air resistance)
    t = 0
    v0 = 2.3
    vy = v0*math.sin(theta_rads)
    vx = v0*math.cos(theta_rads)
    y = 0
    x = 0

    # initial conditions (in vacuum)
    vy_vac = vy
    vx_vac = vx
    y_vac = y
    x_vac = x

    # lists for the motion in air resistance
    timev = [t]
    velocityy = [vy]
    velocityx = [vx]
    yy = [y]
    xx = [x]

    # lists for the motion in vacuum
    velocityy_vac = [vy]
    velocityx_vac = [vx]
    yy_vac = [y]
    xx_vac = [x]


    # loop for the Euler integration
    while(y_vac >= 0):
        
        # model with air resistance
        dvy = -g*dt - (b/m)*vy*dt
        vy += dvy
        
        dy = dt*vy
        y += dy
        
        dvx = -(b/m)*vx*dt
        vx += dvx
        
        dx = dt*vx
        x += dx
        
        t += dt

        # this is required when the object hits the ground (y = 0) and we do not want y to be negative.
        if y < 0:
            x -= dx
            y = 0.0
            vy = 0.0
            vx = 0.0

        #Appending to final list     
        timev.append(t)
        velocityy.append(vy)
        velocityx.append(vx)
        yy.append(y)
        xx.append(x)

        #Iterating y and x values
        dvy_vac = -g*dt
        vy_vac += dvy_vac
        dy_vac = dt*vy_vac
        y_vac += dy_vac
            
        dvx_vac = 0.0
        vx_vac += dvx_vac
        dx_vac = dt*vx_vac
        x_vac += dx_vac
            
        #Position and velocity list     
        velocityy_vac.append(vy_vac)
        velocityx_vac.append(vx_vac)
        yy_vac.append(y_vac)
        xx_vac.append(x_vac)  
    return xx, yy

def quadratic():
    M = 1.0
    g = 9.8
    V = 2.3
    ang = 10.0
    Cd = 0.25
    dt = 0.001
    t = [0]
    vx = [V*np.cos(ang/180*np.pi)]  
    vy = [V*np.sin(ang/180*np.pi)]
    x = [0]                         
    y = [0]
    drag = Cd * V**2
    ax = [-(drag*np.cos(ang/180*np.pi))/M ]          
    ay = [-g-(drag*np.sin(ang/180*np.pi)/M) ]

    count = 0
    while (y[count]>=0):
        t.append(t[count] + dt)
        vx.append(vx[count]+dt*ax[count])  
        vy.append(vy[count]+dt*ay[count])
        x.append(x[count]+dt*vx[count])    
        y.append(y[count]+dt*vy[count])   
        vel = np.sqrt(vx[count+1]**2 + vy[count+1]**2)  
        drag = Cd*vel**2                                 
        ax.append(-(drag*np.cos(ang/180*np.pi))/M)     
        ay.append(-g-(drag*np.sin(ang/180*np.pi)/M))
        count = count + 1
    return x,y
x_v, y_v = vacuum()
x_l, y_l = linear()
x_q, y_q = quadratic()

plt.plot(x_v, y_v, 'r', label='Vacuum')
plt.plot(x_l, y_l, 'b', label='Linear')
plt.plot(x_q, y_q, 'g', label='Quadratic')
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.ylim(0.0, 0.01)
plt.grid()
plt.legend()
plt.show()