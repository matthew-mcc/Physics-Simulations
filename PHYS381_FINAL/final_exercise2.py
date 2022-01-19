import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

initial_state = [0.1, 0, 0]
sigma = 10.
rho = 28.
beta = 8./3

start_time = 0
end_time = 100

t = np.linspace(start_time, end_time, end_time*100)
#diff equations
def deriv(current_state, t, sigma, rho, beta):
    x, y, z = current_state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return dxdt, dydt, dzdt

#integrate over time
result = odeint(deriv, initial_state, t, args=(sigma, rho, beta))
#decompose
x,y,z = result.T


#plot
plt.figure()
plt.plot(x, y, color='r', alpha=0.7, linewidth=0.3)
plt.title("x-y Phase Plane")
plt.show()
plt.plot(x, z, color='g', alpha=0.7, linewidth=0.3)
plt.title("x-z Phase Plane")
plt.show()
plt.plot(y, z, color='b', alpha=0.7, linewidth=0.3)
plt.title("y-z Phase Plane")
plt.show()