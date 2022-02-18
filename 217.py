import matplotlib.pyplot as plt
import numpy as np

xd=np.genfromtxt('xc.txt',dtype='float',delimiter='')
yd=np.genfromtxt('yc.txt',dtype='float',delimiter='')
    
def find_neardata(X,x,y):
    for i in range(x.size):
        if(x[i]<=X):
            x1=x[i]
            x2=x[i+1]
            y1=y[i]
            y2=y[i+1]
    return x1,x2,y1,y2

x1,x2,y1,y2=find_neardata(7,xd,yd)



def ya(X,x,y):
    x1,x2,y1,y2=find_neardata(X, x, y)
    slope=(y2-y1)/(x2-x1)
    distance=(X-x1)
    
    return y1+slope*distance

f=ya(0.22262332313,xd,yd)
print(f)