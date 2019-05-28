# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:51:11 2019

@author: deepali
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

#randomly taken values of pixels for the size of star.
FOVx=FOVy=15
sig=int(input("Input the value of Sigma:"))
m=float(input("magnitude of the star:"))

#flux corresponding to an m magnitude star.
fx=math.pow(10,-1*(m/2.5))*4*math.pow(10,12)

#coordinates of the central pixel.
x0=(FOVx-1)/2 
y0=x0
F=[]
for xi in range(FOVx):
    a=[]
    for yi in range(FOVy):
#formula of a 2D gauss distribution function. 
        k=1/(2*22*math.pow(sig,2)/7)
        g=math.exp(-1*(math.pow((xi-x0),2)+math.pow((yi-y0),2))/(2*math.pow(sig,2)))
#multiplying probability to the total outcomes that is the total flux of the star of magnitude m.
        a.append(g*k*fx)
    F.append(a)

#printing the final matrix  
print("The output matrix is:")
for xi in range(FOVx):
    b=[]   
    for yi in range(FOVy):
        b.append(F[xi][yi])
    np.savetxt('image_data.dat',b)
    print(b)
    
#code for image
color_map=plt.imshow(F)
color_map.set_cmap("Greys_r")
plt.colorbar()
plt.savefig("out.png")

