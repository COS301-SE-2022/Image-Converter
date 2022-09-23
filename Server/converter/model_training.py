import matplotlib.pyplot as plt
import numpy as np
import pathlib
import PIL
import cv2
import schedule
import time
import tensorflow as tf
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Model
from keras.models import load_model

def trainModel():

#######################################################################################
####### Dataset Collection ############################################################
#######################################################################################
    data_dir = (r"C:\Users\moemo\Downloads/graph_dataset")

    img_height,img_width=90,90
    batch_size=32
    #Preprocessing module deprecated, switch to tf.keras.utils.image_dataset_from_directory
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
      data_dir,
      validation_split=0.2,
      subset="training",
      seed=123,
      image_size=(img_height, img_width),
      batch_size=batch_size)

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
      data_dir,
      validation_split=0.2,
      subset="validation",
      seed=123,
      image_size=(img_height, img_width),
      batch_size=batch_size)

    class_names = train_ds.class_names



