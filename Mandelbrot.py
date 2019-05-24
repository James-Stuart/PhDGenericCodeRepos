import time
import numpy as np
from matplotlib.pyplot import *
from matplotlib.colors import LogNorm
from mpl_toolkits import mplot3d
%matplotlib inline

def mandelbrotIter(n,iterMax=5,_iterCur=0,_zOld=0,output=[0]):
    ''' Takes input'''
    if _iterCur < iterMax:
        zNew = _zOld**2+n
        if abs(zNew)  >= 2:
            print(str(n) + ' diverges after ' + str(_iterCur) + ' iterations')
            return output
        
        loop = _iterCur + 1
        output.append(zNew)
        return mandelbrotIter(n,iterMax,loop,zNew,output)
    else:
        return output
    
def mandelbrotDraw(xRange,yRange,xRes,yRes,iterMax=10,plotOn=True):
    ''' Draws the Mandelbrot fractal in a given range with given resolution'''
    x = np.linspace(xRange[0],xRange[1],xRes)
    
    y = np.linspace(yRange[0],yRange[1],yRes)
    c=x[np.newaxis,:]+ 1j*y[:,np.newaxis]
    
    z=np.zeros(c.shape,dtype=np.complex64)
    output = np.zeros(c.shape)
    
    for it in range(iterMax):
        notdone = np.less(z.real*z.real + z.imag*z.imag, 4.0)
        output[notdone] = it
        z[notdone] = z[notdone]**2 + c[notdone]
    output[output == iterMax-1] = 0.01

    if plotOn:
        figure(figsize=[15,10])
        imshow(output, cmap='hot',extent=[xRange[0], xRange[1], yRange[0], yRange[1]])
    print(output.shape)
    return x,y,output
    

x,y,Mset = mandelbrotDraw([-2,1],[-1,1],1000,1000,100)
# x,y,Mset = mandelbrotDraw([-0.2,0],[0.8,1],500,500,100)

# c=-0.5+0.2j
# orbit = mandelbrotIter(c,100)
# plot(np.real(orbit),np.imag(orbit),'b.')
# plot(np.real(c),np.imag(c),'w.')
# colorbar()