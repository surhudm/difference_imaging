import numpy as np
import pylab as pl

# Create a routine which will return an array with an image of a star at a
# given location given its magnitude, position and size of the PSF

def get_star(xx, yy, mag, sigma, Nx, Ny, fluxmag0, skymag_per_pixelsq=0):
    '''
    Returns an image of a star at given array of locations (xx[i], y[i]) in an
    image of size (Nx, Ny) with a given magnitude, position and size of the PSF,
    the total flux of a magnitude zero star.

    mag = -2.5*np.log10(flux/fluxmag0)
    '''

    arr = np.zeros((Nx, Ny))

    '''
    This loop can be made way faster with C++
    '''
    # First define the normalization factor for each star
    fac = np.zeros(xx.size)
    for kk in range(xx.size):
        counts = fluxmag0*10.**(-0.4*mag[kk])
        fac[kk] = counts/(2.0*np.pi*sigma[kk]**2)
    bg = fluxmag0*10.**(-0.4*skymag_per_pixelsq)

    for ii in range(Nx):
        for jj in range(Ny):
            flux = 0
            for kk in range(xx.size):
                flux += fac[kk]*np.exp(-1/2./sigma[kk]**2*((ii-xx[kk])**2 + (jj-yy[kk])**2))

            if (ii==50) & (jj==50):
                print flux, bg
            arr[ii][jj] = np.random.poisson(flux+bg)

    return arr


if __name__ == "__main__":
    xxarr = np.array([50, 40, 30])
    yyarr = np.array([50, 50, 50])
    magarr = np.array([24.5, 25.0, 25.0])
    sigmaarr = np.array([2.5, 2.5, 2.5])
    image1 = get_star(xxarr, yyarr, magarr, sigmaarr, 101, 101, 4e12, 27.0)

    ax = pl.subplot(222)
    im = ax.imshow(np.log10(image1), cmap="Greys_r")
    pl.colorbar(im)

    pl.savefig("Fig.pdf")
