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


#######################################################################################
####### Model Training ################################################################
#######################################################################################        
    resnet_model = Sequential()

    pretrained_model= tf.keras.applications.ResNet50(include_top=False,
                       input_shape=(img_height,img_width,3),
                       pooling='avg',classes=6,
                       weights='imagenet')


    for layer in pretrained_model.layers:
        layer.trainable=False

    resnet_model.add(pretrained_model)

    resnet_model.add(Flatten())
    resnet_model.add(Dense(512, activation='relu'))
    resnet_model.add(Dense(256, activation='relu'))
    resnet_model.add(Dense(128, activation='relu'))
    resnet_model.add(Dense(64, activation='relu'))

    resnet_model.add(Dense(8))

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss',
    patience=3), tf.keras.callbacks.ModelCheckpoint(filepath="model",save_best_weights=True),tf.keras.callbacks.TensorBoard()]

    resnet_model.compile(optimizer=Adam(lr=0.001),loss=loss_fn,metrics=['accuracy'])

    history = resnet_model.fit(train_ds, validation_data=val_ds, epochs=1)

    resnet_model.save("VM_Model")




