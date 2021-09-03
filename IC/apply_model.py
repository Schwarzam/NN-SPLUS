import tensorflow as tf
import keras

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten

from keras.preprocessing.image import ImageDataGenerator
from keras import layers, models
from keras.models import load_model
import random 

import os
from os import listdir
from os.path import isfile, join
from PIL import Image

import cv2
from skimage.io import imread
from sklearn.utils import class_weight

import matplotlib.pyplot as plt
import pandas as pd
import splusdata

conn = splusdata.connect('gustavo', 'Gustavo99!')

model = keras.models.load_model('/home/gustavo/Downloads/modelTradicional.h5')
df = pd.read_csv('https://raw.githubusercontent.com/Schwarzam/Data-analyse---SPLUS-objs/master/DR2_list_fields_reference.cat', delim_whitespace=True)

for field in df['field']:
  res = conn.query(f"""SELECT top 1000 stg.id, stg.ra, stg.dec 
                    FROM idr3_vacs.star_galaxy_quasar AS stg JOIN idr3.r_band AS r on stg.id = r.id
                    WHERE class = 2 and prob_gal > 0.8 AND r.r_auto < 16.5 and r.field = '{field}'""")
    
  nim = []
  for i in res:
    try:
      im = conn.get_img(i['RA'], i['DEC'], 128)
      im = im.convert('RGB')
      im = np.asarray(im)
      im = im / 255.0

      im = im.reshape(128, 128, 3)
      nim.append(im)

    except Exception as e:
      print(e)
      nim.append(np.zeros((128, 128, 3)))
      continue



  nim = np.asarray(nim)
  prds = model.predict(nim)

  ind = np.where(prds > 0.7)[0]
  res[ind].write(f'predict/catalogs/{field}.csv', format='csv')
  selected_res = res[ind]

  for key, value in enumerate(nim[ind]):
    h = Image.fromarray((nim[ind][key] * 255).astype('uint8'))
    h.save(f"predict/images/{selected_res[key]['ID']}.png")

  print(f'finished {field}')