import scipy.optimize
from scipy.optimize import curve_fit
import math 
import numpy as np
import matplotlib.pyplot as plt

#HELIUM FILE
oscillation_open = open('damped_oscillation.txt', 'r')
oscillation = oscillation_open.readlines()
oscillation_open.close()

guess = np.array([10, 10, 10, 10, 10])
x_vals = []
y_vals = []

#loop for splitting
for i in oscillation:
    col = i.split()
    x_vals.append(float(col[0]))
    y_vals.append(float(col[1]))

x_data = np.asarray(x_vals)
y_data = np.asarray(y_vals)

theta0, beta, omega, phi, gamma = guess

def theta_time(t, theta0, beta, omega, phi, gamma):
    func = theta0 * np.exp(-beta*t)*np.cos(omega*t + phi) + gamma
    return func

popt, pcov = curve_fit(theta_time, x_data, y_data, p0=guess)

theta0_new = popt[0]
beta_new = popt[1]
omega_new = popt[2]
phi_new = popt[3]
gamma_new = popt[4]

time = np.linspace(min(x_data), max(x_data), 50)

plt.plot(x_data, y_data, 'b', label="Text File")
plt.plot(time, theta_time(time, theta0_new, beta_new, omega_new, phi_new, gamma_new), 'ro', label="Curve Fitting")
plt.title("Damped Harmonic Oscillator")
plt.grid()
plt.legend()
plt.show()