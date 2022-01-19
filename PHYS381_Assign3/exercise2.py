import numpy
import matplotlib.pylab as plt

#delta_vy = g * delta_t - b/m * vy*delta_t

g = 9.81
D = 10 * (10 ** -4)
B = 1.6 * (10**-4)
m = 2.0 * (10**-3)

t = 0
dt = 0.25
vy = 0
dvy = 0.25

t_list = []
vy_list = []

while t <= 1:
    dvy = g * dt - (B/m) * vy * dt
    vy = vy + dvy
    vy_list.append(vy)
    t = t + dt
    t_list.append(t)
print(vy_list)
plt.plot(t_list, vy_list)
plt.show()