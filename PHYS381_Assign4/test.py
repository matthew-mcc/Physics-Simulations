re_l = []
im_l = []
signal_l = []
m = 0
n = 0
n_l = []
for m in range(N):
    re, im, signal = 0.0, 0.0, 0.0
    
    for n in range(N):
        re = math.sin(0.45*math.pi*m*h) * math.cos(2*math.pi*n*m/N)
        re_l.append(re)
        im = math.sin(0.45*math.pi*m*h) * math.sin(2*math.pi*n*m/N)
        im_l.append(im)
        signal = (re * math.cos(2*math.pi*m*n/N)) + (im * math.sin(2*math.pi*m*n/N))
        signal_l.append(signal)
       
        n_l.append(n)
    
        