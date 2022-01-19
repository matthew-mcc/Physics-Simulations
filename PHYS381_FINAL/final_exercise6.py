import numpy as np
import matplotlib.pylab as plt

def quadratic():
    M = 0.046 #kg
    g = 9.81 #m/s^2
    v0 = 60 #m/s
    ang = 50.0 #degrees
    Cd = (0.25 * (43e-3)**2) #drag coeff
    dt = 0.001 #delta t
    t = [0] #t list
    vx = [v0*np.cos(ang/180*np.pi)] #vx initial
    vy = [v0*np.sin(ang/180*np.pi)] #vy initial
    x = [0] #x initial                         
    y = [0] #y initial
    drag = Cd * v0**2 #drag
    ax = [-(drag*np.cos(ang/180*np.pi))/M ] #acceleration initial x         
    ay = [-g-(drag*np.sin(ang/180*np.pi)/M) ] #acceleration inital y

    count = 0
    #Projectile motion under quadratic drag iteration 
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
    return x,y, t[-1]
#redfine to call functions 

x_q, y_q, time_taken = quadratic()
print("The time taken:", time_taken)

def space_invader(time_taken):
    dt = 0.001
    t = [0]
    x = [150]
    y = [30]
    vx = -10
    count = 0
    while t[count] <= time_taken:
        t.append(t[count] + dt)
        x.append(x[count] + dt*vx)
        y.append(y[count])
        count = count + 1
    return x,y


x_si, y_si = space_invader(time_taken)
#plot vacuum, linear, and quadratic motion on same graph

plt.plot(x_q, y_q, 'b', label='Quadratic')
plt.plot(x_si, y_si, 'r', label="Space Invader")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.grid()
plt.legend()
plt.show()