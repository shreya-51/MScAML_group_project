from tabnanny import verbose
from pandas import Categorical
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D


# LeNet-5 model
def get_img_model(input_shape, num_classes):
    model = Sequential()
    model.add(Conv2D(6, kernel_size=(3, 3), activation="relu", strides=(1, 1), input_shape=input_shape, padding="same"))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
    model.add(Conv2D(16, kernel_size=(3, 3), activation="relu", strides=(1, 1), padding="same"))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
    model.add(Flatten())
    model.add(Dense(120, activation="relu"))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(num_classes, activation="softmax"))
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

