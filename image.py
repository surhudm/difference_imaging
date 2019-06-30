#only to generate a single star.
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:51:11 2019

@author: deepali

"""
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def single_star(FOVx, FOVy, m, zeromag, sig, skymag_per_pixelsq=0):
	#randomly taken values of pixels for the size of star.
	#FOVx=FOVy=15
	#sig=int(input("Input the value of Sigma:"))
	#m=float(input("magnitude of the star:"))
	
	I_matrix = np.zeros((FOVx,FOVy))
	#flux corresponding to an m magnitude star.
	fx=math.pow(10,-1*(m/2.5))*zeromag
	
	#coordinates of the central pixel.
	x0=(FOVx-1)/2 
	y0=x0
	bg = zeromag*10.**(-0.4*skymag_per_pixelsq)
	
	for xi in range(FOVx):
	    for yi in range(FOVy):
	#formula of a 2D gauss distribution function. 
	        k=1/(2*np.pi*math.pow(sig,2))
	        g=math.exp(-1*(math.pow((xi-x0),2)+math.pow((yi-y0),2))/(2*math.pow(sig,2)))
	#multiplying probability to the total outcomes that is the total flux of the star of magnitude m.
	        I_matrix[xi][yi]=np.random.poisson((g*k*fx)+bg)
	np.savetxt('image_data.dat',I_matrix)
	
	print("The output matrix is:")
	for xi in range(FOVx):
	    b=[]   
	    for yi in range(FOVy):
	        b.append(I_matrix[xi][yi])
	    print(b)
	return(I_matrix)
	'''
	#printing the final matrix  
	
	print("The output matrix is:")
	for xi in range(FOVx):
	    b=[]   
	    for yi in range(FOVy):
	        b.append(F[xi][yi])
	   
	    print(b)
	    
	#code for image
	#color_map=plt.imshow(F)
	#color_map.set_cmap("Greys_r")
	#plt.colorbar()
	#plt.savefig("out.png")
	'''
def kernel_con(FOVx, FOVy,  sig1, sig2):
	kernel= np.zeros((FOVx,FOVy))
	x0=(FOVx-1)/2 
	y0=(FOVy-1)/2

	sig=math.sqrt((sig1**2-sig2**2))
	print sig
	for xi in range(FOVx):
		for yi in range(FOVy):
	#formula of a 2D gauss distribution function. 
	        	k=1/(2*np.pi*math.pow(sig,2))
	        	g=math.exp(-1*(math.pow((xi-x0),2)+math.pow((yi-y0),2))/(2*math.pow(sig,2)))
	#multiplying probability to the total outcomes that is the total flux of the star of magnitude m.
	        	kernel[xi][yi]=g*k
	return (kernel)
