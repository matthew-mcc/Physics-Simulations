import scipy.optimize
from scipy.optimize import curve_fit
import math 
import numpy as np
import matplotlib.pyplot as plt

#HELIUM FILE
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

helium_sigma = 
plt.plot(x_data, y_data, 'bo', label="Text File")
plt.plot(X, LJ_pot(X, sigma_2, epsilon_2), 'r', label="Curve Fitting")
plt.title("Helium Leonard Jones Potential")
plt.grid()
plt.legend()
plt.show()

#ARGON FILE
argon_open = open('potential_Ar2_QM.txt', 'r')
argon = argon_open.readlines()
argon_open.close()

guess = np.array([10, 10])
x_vals = []
y_vals = []

#loop for splitting
for i in argon:
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
plt.title("Argon Leonard Jones Potential")
plt.grid()
plt.legend()
plt.show()

#Krypton FILE
krypton_open = open('potential_Kr2_QM.txt', 'r')
krypton = krypton_open.readlines()
krypton_open.close()

guess = np.array([10, 10])
x_vals = []
y_vals = []

#loop for splitting
for i in krypton:
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
plt.title("Krypton Leonard Jones Potential")
plt.grid()
plt.legend()
plt.show()

#Neon File
neon_open = open('potential_Ne2_QM.txt', 'r')
neon = neon_open.readlines()
neon_open.close()

guess = np.array([10, 10])
x_vals = []
y_vals = []

#loop for splitting
for i in neon:
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
plt.title("Neon Leonard Jones Potential")
plt.grid()
plt.legend()
plt.show()

#Part B!
#lets use newton raphson
epsilon = epsilon_2 #kj/mol
sigma = sigma_2 #Angs

tol = 1e-4

#define all functions for NR method
# 1 the lennard jones pot
# 2 the force (-dV/dr)
# 3 Second derivative of V(r)

def v(x):
    #Lennard jones potential
    return 4*epsilon * ((sigma/x)**12 - (sigma/x)**6)

def dv(x):
    #first derivative of V(x)
    return 4*epsilon * (sigma**12 * (-12)*x**(-13) - sigma**6 * (-6)*x**(-7))

def d2v(x):
    #second derivative of v(x)
    return 4*epsilon * (sigma**12 * (-12)*(-13)*x**(-14) - sigma**6 * (-6)*(-7)*x**(-8))

#array of r values: (seperation)


r = np.arange(0.01, 10.0, 0.01)

#force array fore sake of plotting
force = -dv(r)
#initial conditions for NR method
r0 = 0.2 #angs
nsteps = 0

#lists to store computed seperations from NR, the potential and the force
list_r = [r0]
list_v = [v(r0)]
list_f = [-dv(r0)]

#initiating NR BlocK UNTIL abs(dv(x)) < tol

while abs(dv(r0)) > tol:
    nsteps += 1
    r0 = r0 - dv(r0)/d2v(r0)

    list_r.append(r0)
    list_v.append(v(r0))
    list_f.append(-dv(r0))

#plotting
#plot of potential plus convergance to minimum
plt.figure()
plt.xlabel( "(A)")
plt.ylabel('V(r) (kJ/mol)')
plt.grid()
plt.plot(r_vals, v(r_vals), linewidth=2)
plt.plot(list_r, list_v, 'rs--')
plt.show()