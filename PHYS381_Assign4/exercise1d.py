import matplotlib.pylab as plt
import math
import numpy as np
from scipy.signal import square

# Copy here the simpson integration function done in class
def simpson(fun, a, b, n):
    h = (b-a)/float(n)
    
    x0 = a
    xn = b
    
    y0 = fun(x0)
    yn = fun(xn)
    
    # sum over even indexes of x and sum over odd indexes of x
    feven = 0.0
    fodd = 0.0
    
    for j in range(2,n,2):
        print(j)
        xeven = a + j*h
        feven += fun(xeven)
        
        xodd = a + (j-1)*h
        fodd += fun(xodd)
        
    # range method above does not include the last odd term
    xodd = a + (n-1)*h
    fodd += fun(xodd)
    
    intfun = h*(y0 + 2.0*feven + 4.0*fodd + yn)/3.0
    
    return intfun




# Define parameters for the problem (omega = 1 and T is the period)

duty = 0.6
alpha = 1.0/duty
omega = 1.0
T = 2 * math.pi / omega

# limits of the integration
a = 0.0
b = T

# number of points to calculate the integral (50 integration elements may be sufficient)
n = 50

# Number of coefficients to be calculated (set up to 10 coefficients for now)
nc = 20
thetas = np.linspace(0,T,1000, endpoint=False)


# define the function that will be expanded in terms of Fourier series
#uncomment whichever function you want to examine
def function(thetas):
    return square(thetas, duty=duty)
ftheta = function(thetas)
# calculate the coefficient a_0 first! That is just integrating the function directly over the interval [a,b]
#need to use simpson function
simpson_func = simpson(function, a, b, n)
#a0 = simpson_func/T
a0 = (2/alpha) - 1

# Initiate lists that will store all Fourier coeffcients (k=0 and k>0). 
# But we can store already our a0 coefficient on the list.
a_manual_list = [a0]
b_manual_list = [0.0]

# define functions that will calculate all other coefficients
#def fak(thetas):
#    return function(thetas) * math.cos(k*thetas)

def fak(thetas):
    return((2/k*math.pi) * (math.sin(2*k*math.pi/alpha)))

#def fbk(thetas):
#    return function(thetas) * math.sin(k*thetas)
def fbk(thetas):
    return((2/k*math.pi) * (1 - (math.cos(2*k*math.pi/alpha))))


# All functions defined above are 'idle'. We are now going to loop over the coefficients components
# to calculate all other coefficients from k=1 upt to k=nc. Just use a simple for-loop for that.
# for-loop over number of coefficients

for k in range (1, nc):
    simpson_func = simpson(fak, a, b, n)

    ak = 2 * simpson_func / T
    a_manual_list.append(ak)

    simpson_func = simpson(fbk, a, b, n)

    bk = 2 * simpson_func / T
    b_manual_list.append(bk)

    print('a%s='%k, ak, ' b%s='%k, bk)
# After the loop is completed and new coefficients are appended on the lists, 
# add plot instructions that will make a graphic for a_k and b_k versus k in the same panel.

#plotting f(theta) x theta
#plt.plot(range(), ftheta, marker='o')
#plt.plot(range(nc), thetas, marker='*')

plt.plot(thetas, ftheta)

plt.show()