import create_image as ci
import numpy as np
import pylab as pl

np.random.seed(12313)

xxarr = np.array([50, 40, 30])
yyarr = np.array([50, 50, 50])
magarr = np.array([24.5, 25.0, 25.0])
sigmaarr = np.array([2.5, 2.5, 2.5])
image = ci.get_star(xxarr, yyarr, magarr, sigmaarr, 101, 101, 4e12, 29.0)

ax = pl.subplot(222)
im = ax.imshow(np.log10(image), cmap="Greys_r")
pl.colorbar(im)

pl.savefig("Fig.pdf")
