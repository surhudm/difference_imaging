'''
There is always a place for possibilities
And there is definitely place to improve this program.
'''
import create_image as ci
import numpy as np
import pylab as pl
import sys
import matplotlib.pyplot as plt 
import random
import math
import scipy as scipy
from scipy import signal


'''
To generate a series of images in which the magnitude of only one star is varying according to a portion of 
the light curve of an RR Lyrae star.
considerations:
The magnitude of that star in the template(temp) image is maximum i.e. the flux is minimum.
The first image is the template image.
The psf is changing randomly between 2.5 and 4.28 in the images.
 
'''

#convert   -delay 20   -loop 0   sphere*.png   animatespheres.gif
#fname=sys.argv[1]
z2=[]
z1=[]
b=[]
y=[23.6]
np.random.seed(12313)
image_num=14

for i in range(image_num):
    '''
    Trying to vary the magnitude of the star according to a portion of the light curve of the RR Lyrae star. 
    The function for the same is given below.
    ''' 
    x=0.1 + 1./40*((i-5)**2 - 3*(i-5))
    p=random.uniform(0.1, 1.78)
    z2.append(i-5)
    b.append(x+22.5)    
    if i==0:
        p=0
    xxarr = np.array([50, 70, 30, 30, 25, 11, 56, 80, 105, 135, 145, 90, 100, 130, 10, 115])
    yyarr = np.array([50, 60, 65, 20, 30, 145, 130, 22, 45 ,95, 80, 30, 115, 10, 95, 20])
    magarr = np.array([24.5, 25.0, 23.0, 24.0, 24.5, 23, 24.5, 24.0, 23.0, 22.5+x, 25.0, 22.0, 24.0, 23.0, 22.5, 25.0])
    sigmaarr = np.array([2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p])
    
    image = ci.get_star(xxarr, yyarr, magarr, sigmaarr, 151, 151, 4e12, 29.0)

#image
    fname = "image_%03d.png" % i
    ci.myplot(np.log10(image), fname, 0.0, 2.5, i)
    if i==0:
        temp=image
        continue

#image-temp
    fname = "diff_image_%03d.png" % i
    ci.myplot(image-temp, fname, -32., 32.0, i, True)


#convolution kernel
    con=ci.kernel_con(21, 21, 2.5+p, 2.5)
    con = con/np.sum(con)#normalizing the convolution kernel.

#convolved image
    final=scipy.signal.convolve2d(temp, con, mode='same', boundary='fill', fillvalue=0)

#convolved image(final)-image
    fname = "con_diff_image_%03d.png" % i
    ci.myplot(final-image, fname, -32., 32.0, i, True)
    
#To plot te manitude of te star(xxarr[9], yyarr[9])
    d=image-temp
    sum1=0.0
    '''
    summing-up the flux within a square of 12x12.
    '''
    for q in range(12):
        for j in range(12):
            sum1=sum1+d[xxarr[9]-5+q][yyarr[9]-5+j]#just by changing the value at '9', the star can be changed.
    sum2=sum1+(4e12*pow(10,-1*23.6/2.5))
    m=-1*2.5*np.log10(np.abs(sum2/4e12))
    
    y.append(m)
    z1.append(i-5)

plt.plot(z2,y,'r')
plt.plot(z2,b,'g')#Reference light curve that is of RR Lyrae

plt.savefig('lit_Curve.png')

