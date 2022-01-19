import numpy as np
import matplotlib.pylab as plt
# plot f(v) = bc + cv^2 - but we are actually plotting coefficients seperately

B = 1.6 * (10**-4)
C = 0.25

D = 1
def v_lin(B, D, v):
    x = D * v
    return B * x
def v_quad(C, D, v):
    x = D * v
    return C * x * x

v_lin_l = np.array([])
v_quad_l = np.array([])
x = np.arange(0.0, 0.01 , 0.01)
for i in range(0, 100):
    v_lin_l = np.append(v_lin_l, v_lin(B,D,x[i]))
    v_quad_l = np.append(v_quad_l, v_quad(C,D,x[i]))


plt.plot(x, v_lin_l)
plt.plot(x, v_quad_l)
plt.xlabel("v")
plt.ylabel("f(v)")
plt.grid()
plt.show()