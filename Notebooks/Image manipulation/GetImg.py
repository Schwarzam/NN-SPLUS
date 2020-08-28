from astropy.io import fits
from astropy.visualization import make_lupton_rgb
import matplotlib.pyplot as plt

def get_img(name, stretch):
    PATH_G = "/Users/schwarzam/Documents/cutouts"
    PATH_R = "/Users/schwarzam/Documents/cutouts"
    PATH_I = "/Users/schwarzam/Documents/cutouts"

    print(PATH_G)

    image_fileG = f'{PATH_G}/{name}_G.fits'
    image_dataG = fits.getdata(image_fileG, ext=0)
    image_fileR = f'{PATH_R}/{name}_R.fits'
    image_dataR = fits.getdata(image_fileR, ext=0)
    image_fileI = f'{PATH_I}/{name}_I.fits'
    image_dataI = fits.getdata(image_fileI, ext=0)

    image = make_lupton_rgb(image_dataI, image_dataR, image_dataG, stretch=stretch, Q=5)

    return image

def get_img_paths(nameG, nameR, nameI, stretch):
    image_fileG = f'{nameG}'
    image_dataG = fits.getdata(image_fileG, ext=0)
    image_fileR = f'{nameR}'
    image_dataR = fits.getdata(image_fileR, ext=0)
    image_fileI = f'{nameI}'
    image_dataI = fits.getdata(image_fileI, ext=0)

    image = make_lupton_rgb(image_dataI, image_dataR, image_dataG, stretch=stretch, Q=5)
    return image

import os
from os import listdir
from os.path import isfile, join
import numpy as np

mypath = "/Users/schwarzam/Documents/cutouts/"
onlyfiles = os.listdir(mypath)

for direc in onlyfiles:
    arrayofnames = list(range(9))
    try:
        newpath = f'{mypath}/{direc}'
        dirfiles = [f for f in listdir(newpath) if isfile(join(newpath, f))]

        for files in dirfiles:
            splitted = files.split('_')

            if arrayofnames[3] == 3 and (arrayofnames[2] == 2 or arrayofnames[1] == 1 or arrayofnames[0] == 0):
                if splitted[2] == 'R' and splitted[4] == 'swp.fits':
                    arrayofnames[1] = files
                if splitted[2] == 'G' and splitted[4] == 'swp.fits':
                    arrayofnames[0] = files
                if splitted[2] == 'I' and splitted[4] == 'swp.fits':
                    arrayofnames[2] = files

            if arrayofnames[0] != 0 and arrayofnames[1] != 1 and arrayofnames[2] != 2:
                if splitted[2] == 'R' and splitted[4] == 'swp.fits':
                    arrayofnames[4] = files
                if splitted[2] == 'G' and splitted[4] == 'swp.fits':
                    arrayofnames[3] = files
                if splitted[2] == 'I' and splitted[4] == 'swp.fits':
                    arrayofnames[5] = files

            if arrayofnames[0] != 0 and arrayofnames[1] != 1 and arrayofnames[2] != 2:
                image = get_img_paths(f'{newpath}/{arrayofnames[0]}',
                                      f'{newpath}/{arrayofnames[1]}',
                                      f'{newpath}/{arrayofnames[2]}',
                                      stretch=1.3)

                plt.imsave(arr=image, fname=f'/Users/schwarzam/Documents/Stamps/fornax/{direc}.png')

    except:
        pass

image = get_img_paths('/Users/schwarzam/Documents/cutouts/FCC00008/FCC00008_s26s32_G_256x256_swp.fits',
                      '/Users/schwarzam/Documents/cutouts/FCC00008/FCC00008_s26s32_R_256x256_swp.fits',
                      '/Users/schwarzam/Documents/cutouts/FCC00008/FCC00008_s26s32_I_256x256_swp.fits',
                      stretch=3)

plt.imshow(image)
plt.imsave(arr = image, fname='/Users/schwarzam/Documents/Stamps/fornax/FCC00008_s26s32_256x256_swp.png')

plt.show()


def get_list():
    escolha = ['ISOarea',
               's2nDet',
               'PhotoFlag',
               'FWHM',
               'FWHM_n',
               'MUMAX',
               'A',
               'B',
               'THETA',
               'FlRadDet',
               'KrRadDet',
               'nDet_auto',
               'nDet_petro',
               'nDet_aper',
               'uJAVA_auto',
               'euJAVA_auto',
               's2n_uJAVA_auto',
               'uJAVA_petro',
               'euJAVA_petro',
               's2n_uJAVA_petro',
               'uJAVA_aper',
               'euJAVA_aper',
               's2n_uJAVA_aper',
               'F378_auto',
               'eF378_auto',
               's2n_F378_auto',
               'F378_petro',
               'eF378_petro',
               's2n_F378_petro',
               'F378_aper',
               'eF378_aper',
               's2n_F378_aper',
               'F395_auto',
               'eF395_auto',
               's2n_F395_auto',
               'F395_petro',
               'eF395_petro',
               's2n_F395_petro',
               'F395_aper',
               'eF395_aper',
               's2n_F395_aper',
               'F410_auto',
               'eF410_auto',
               's2n_F410_auto',
               'F410_petro',
               'eF410_petro',
               's2n_F410_petro',
               'F410_aper',
               'eF410_aper',
               's2n_F410_aper',
               'F430_auto',
               'eF430_auto',
               's2n_F430_auto',
               'F430_petro',
               'eF430_petro',
               's2n_F430_petro',
               'F430_aper',
               'eF430_aper',
               's2n_F430_aper',
               'g_auto',
               'eg_auto',
               's2n_g_auto',
               'g_petro',
               'eg_petro',
               's2n_g_petro',
               'g_aper',
               'eg_aper',
               's2n_g_aper',
               'F515_auto',
               'eF515_auto',
               's2n_F515_auto',
               'F515_petro',
               'eF515_petro',
               's2n_F515_petro',
               'F515_aper',
               'eF515_aper',
               's2n_F515_aper',
               'r_auto',
               'er_auto',
               's2n_r_auto',
               'er_petro',
               's2n_r_petro',
               'r_aper',
               'er_aper',
               's2n_r_aper',
               'F660_auto',
               'eF660_auto',
               's2n_F660_auto',
               'F660_petro',
               'eF660_petro',
               's2n_F660_petro',
               'F660_aper',
               'eF660_aper',
               's2n_F660_aper',
               'i_auto',
               'ei_auto',
               's2n_i_auto',
               'i_petro',
               'ei_petro',
               's2n_i_petro',
               'i_aper',
               'ei_aper',
               's2n_i_aper',
               'F861_auto',
               'eF861_auto',
               's2n_F861_auto',
               'F861_petro',
               'eF861_petro',
               's2n_F861_petro',
               'F861_aper',
               'eF861_aper',
               's2n_F861_aper',
               'z_auto',
               'ez_auto',
               's2n_z_auto',
               'z_petro',
               'ez_petro',
               's2n_z_petro',
               'z_aper',
               'ez_aper',
               's2n_z_aper',
               'Tb',
               'Odds',
               'Chi2',
               'M_B',
               'Stell_Mass',
               'CLASS',
               'PROB_GAL',
               'PROB_STAR',
               'RA_WISE',
               'Dec_WISE',
               'w1mpro',
               'w1sigmpro',
               'w1snr',
               'w1sat',
               'w2mpro',
               'w2sigmpro',
               'w2snr',
               'w2sat',
               'var_flg',
               'ph_qual',
               'simple_class_y'
               ]
    return escolha