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

IMAGE_SIZE = 1000

PATH = "/home/gustavo/Documents/images/"

ra = input("RA: ")
dec = input("DEC: ")

def save_im(colorim, file, name):
    plt.figure(figsize=(15,15))
    ax = plt.subplot(projection=WCS(file[1].header), label='overlays')

    ax.imshow(colorim, origin='lower')

    ax.coords[0].set_axislabel('Galactic Longitude')
    ax.coords[1].set_axislabel('Galactic Latitude')

    overlay = ax.get_coords_overlay('fk5')
    overlay[0].set_axislabel('Right Ascension (J2000)')
    overlay[1].set_axislabel('Declination (J2000)')

    plt.savefig(f'{name}')
    plt.draw()



nim = conn.get_cut(ra, dec, IMAGE_SIZE, band="R")
color = conn.twelve_band_img(ra, dec, IMAGE_SIZE)

save_im(color, nim, os.path.join(PATH, f'{ra}-{dec}.jpg'))
