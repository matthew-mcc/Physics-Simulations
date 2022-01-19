#Exercise 1a:
import numpy as np
import math


def f(x):
    # remember: functions need a return.
    return np.exp(x)


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

# integration test
a = 0.0
b = 1.0
n = 100

Int_simp = simpson(f, a, b, n)

Int_analytical = math.exp(1.0) - 1.0

error = abs(Int_analytical - Int_simp)

print('----------------------------------------------')

print(Int_simp, Int_analytical, error)

        
    