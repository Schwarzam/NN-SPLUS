import splusdata 
import os
import matplotlib.pyplot as plt

from astropy.wcs import WCS

from astropy.nddata import Cutout2D
from astropy.coordinates import SkyCoord

from astropy.io import fits

import astropy.units as u

user = input('Input splus user: ')
password = input('Input splus password: ')
conn = splusdata.connect(user, password)

field = input('Input field: ')

IMAGE_X = [2000, 9000]
IMAGE_Y = [2000, 9000]
IMAGE_SIZE = 1000

im = conn.get_field(field, 'R')

PATH = "/home/gustavo/Documents/images/"


def cut(f, ra, dec, size=1000):

    wcs = WCS(f[1].header)
    pos = SkyCoord(ra*u.deg,dec*u.deg)
    d = Cutout2D(f[1].data, pos, [size, size], wcs)
    nfits = fits.PrimaryHDU(data=d.data, header=d.wcs.to_header())
    
    colored_im = conn.twelve_band_img(ra,dec, size)
    return nfits, colored_im

def cut_from_pixel(f, ra, dec, size=1000):

    wcs = WCS(f[1].header)
    
    ra = wcs.pixel_to_world(ra, dec).ra.deg * u.deg
    dec = wcs.pixel_to_world(ra, dec).dec.deg * u.deg
    
    pos = SkyCoord(ra, dec)
    d = Cutout2D(f[1].data, pos, [size, size], wcs)
    nfits = fits.PrimaryHDU(data=d.data, header=d.wcs.to_header())

    colored_im = conn.twelve_band_img(float(ra.base), float(dec.base), size)
    return nfits, colored_im

def save_im(colorim, file, name):
    plt.figure(figsize=(15,15))
    ax = plt.subplot(projection=WCS(file.header), label='overlays')

    ax.imshow(colorim, origin='lower')

    ax.coords[0].set_axislabel('Galactic Longitude')
    ax.coords[1].set_axislabel('Galactic Latitude')

    overlay = ax.get_coords_overlay('fk5')
    overlay[0].set_axislabel('Right Ascension (J2000)')
    overlay[1].set_axislabel('Declination (J2000)')

    plt.savefig(f'{name}')
    plt.draw()

x = IMAGE_X[0]
while x <= IMAGE_X[1]:
    y = IMAGE_Y[0]
    while y <= IMAGE_Y[1]:
        
        nim, color = cut_from_pixel(im, x, y, IMAGE_SIZE)
        save_im(color, nim, os.path.join(PATH, f'{x}-{y}-{field}.jpg'))
        
        y += IMAGE_SIZE
    x += IMAGE_SIZE