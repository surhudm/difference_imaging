import create_image as ci
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import sys 
fname=sys.argv[1]

np.random.seed(12313)

xxarr = np.array([50, 40, 30])
yyarr = np.array([50, 50, 50])
magarr = np.array([24.5, 25.0, 25.0])
sigmaarr = np.array([2.5, 2.5, 2.5])
image1 = ci.get_star(xxarr, yyarr, magarr, sigmaarr, 101, 101, 4e12, 29.0)

ax1 = pl.subplot(221)
im1 = ax1.imshow(np.log10(image1), cmap="Greys_r")
pl.colorbar(im1)


xxarr = np.array([50, 40, 30])
yyarr = np.array([50, 50, 50])
magarr = np.array([24.5, 25.0, 0.0])
sigmaarr = np.array([2.5, 2.5, 2.5])
image2 = ci.get_star(xxarr, yyarr, magarr, sigmaarr, 101, 101, 4e12, 29.0)

ax2 = pl.subplot(222)
im2 = ax2.imshow(np.log10(image2), cmap="Greys_r")

pl.colorbar(im2)
ax3 = pl.subplot(223)
im3 = ax3.imshow((image2-image1), cmap="Greys_r")
pl.colorbar(im3)

#color_map=plt.imshow(np.abs(np.subtract(image1,image2)))
#color_map.set_cmap("Greys_r")
#plt.colorbar()
pl.savefig(fname)
pl.clf()

