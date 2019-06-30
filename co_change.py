'''
There is always a place for possibilities
And there is definitely place to improve this program.
'''
import create_image as ci
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import sys 
import math
import random
import scipy as scipy
from scipy import signal
#fname=sys.argv[1]

np.random.seed(12313)
image_num=14

for i in range(image_num):
    p=random.uniform(0.1, 1.78)
    co=5*i
    
    if i==0:
        p=0
		
    xxarr = np.array([50, 70, 30, 30, 25, 11, 56, 80, 105, 135-co, 145, 90, 100, 130, 10, 115])
    yyarr = np.array([50, 60, 65, 20, 30, 145, 130, 22, 45 ,95-co, 80, 30, 115, 10, 95, 20])
    magarr = np.array([24.5, 25.0, 23.0, 27.0, 24.5, 23, 24.5, 24.0, 23.0, 22.5, 25.0, 22.0, 24.0, 23.0, 22.5, 25.0])
    sigmaarr = np.array([2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p, 2.5+p])
    image = ci.get_star(xxarr, yyarr, magarr, sigmaarr, 151, 151, 4e12, 29.0)
	
#image
    fname = "image_%03d.png" % i
    ci.myplot(np.log10(image), fname, 0.0, 2.5, i)
    
    if i==0:
        temp=image
        continue
	
#temp-image
    fname = "co_diff1_%03d.png" % i
    ci.myplot(temp-image, fname, -32., 32.0, i, True)
	
#convolution
    con=ci.kernel_con(21, 21, 2.5+p, 2.5)
#To normalize the kernel
    con = con/np.sum(con)

#convolved name-final
    final=scipy.signal.convolve2d(temp, con, mode = 'same', boundary = 'fill', fillvalue = 0)
	
    fname = "co_diff2_%03d.png" % i
    ci.myplot(final-image, fname, -32.0, 32.0, i, True)






	
