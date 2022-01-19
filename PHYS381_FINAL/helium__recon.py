import scipy.optimize
from scipy.optimize import curve_fit
import math 
import numpy as np
import matplotlib.pyplot as plt

helium_open = open('potential_He2_QM.txt', 'r')
helium = helium_open.readlines()
helium_open.close()

guess = np.array([10, 10])
x_vals = []
y_vals = []

#loop for splitting
for i in helium:
    col = i.split()
    x_vals.append(float(col[0]))
    y_vals.append(float(col[1]))

x_data = np.asarray(x_vals)
y_data = np.asarray(y_vals)

sigma, epsilon = guess

def LJ_pot(r, sigma, epsilon):
    U = 4 * epsilon * ((sigma/r)**12 - (sigma/r)**6)
    return U

popt, pcov = curve_fit(LJ_pot, x_data, y_data, p0=guess)

sigma_2 = popt[0]
epsilon_2 = popt[1]
X = np.linspace(min(x_data), max(x_data), 50)

plt.plot(x_data, y_data, 'bo', label="Text File")
plt.plot(X, LJ_pot(X, sigma_2, epsilon_2), 'r', label="Curve Fitting")
plt.title("Helium Leonard Jones Potential")
plt.grid()
plt.legend()
plt.show()