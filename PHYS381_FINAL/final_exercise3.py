import matplotlib.pyplot as plt
import numpy as np

#SEED USED: 7812394
#TEMP OF LEFT(X=0): 3.5
#TEMP OF RIGHT(X=L): 103.1
#THE TOTAL LENGTH = 10


#1st dimension x 
def Temp_x(iter):
    
    ax = plt.gca()
    xarr = np.linspace(0, 10.0, 100)

    Tarr = np.zeros(len(xarr))

    Tarr[0],Tarr[-1] = 3.5, 103.1
    
    store_list = []

    for i in range(iter):
 
        Tarr[1:-1] = (Tarr[0:-2]+Tarr[2:])/2

        if (i % (iter//5) == 0):
            d = {}
            ax.plot(xarr, Tarr, label=str(i))
            d[i] = list(Tarr)
            store_list.append(d)
          
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("T")
    plt.grid()
    plt.show()
    return store_list

d = Temp_x(6000)

#print(d)
store_1 = d[0]
store_2 = d[1]
store_3 = d[2]
store_4 = d[3]
store_5 = d[4]
xarr = np.linspace(0, 10.0, 100)

def analytic(x):
    l = []    
    for i in range(0, len(x)):
        l.append(9.96 * x[i] + 3.5)
    return l

#analyticitcal: y = 9.96x + 3.5

def error(list1, list2):
    return_list = []
    for i in range(0, len(list1)):
        return_list.append(abs(list1[i]-list2[i]))
    return return_list

plt.plot(xarr, error(analytic(xarr), store_1[0]), label='0')
plt.plot(xarr, error(analytic(xarr), store_2[1200]), label='1200')
plt.plot(xarr, error(analytic(xarr), store_3[2400]), label='2400')
plt.plot(xarr, error(analytic(xarr), store_4[3600]), label='3600')
plt.plot(xarr, error(analytic(xarr), store_5[4800]), label='4800')
plt.ylabel("Error")
plt.xlabel("X")
plt.grid()
plt.legend()
plt.show()



