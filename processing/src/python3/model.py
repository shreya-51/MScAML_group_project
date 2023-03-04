from tabnanny import verbose
from pandas import Categorical
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from load_data import load_spectrograms
from convert_to_c import hex_to_c_array
import matplotlib.pyplot as plt
import os
import sys

img_path = "/Users/matt/Documents/Imperial College London/Modules/Applied Machine Learning Group Project/MScAML_group_project/processing/img_dataset"
random_state = 1
num_classes = 10
epochs = 100
batch_size = 32

X, y = load_spectrograms(img_path)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=random_state)

input_shape = X_train[0].shape


# LeNet-5 model
model = Sequential()
model.add(Conv2D(6, kernel_size=(3, 3), activation="relu", strides=(1, 1), input_shape=input_shape, padding="same"))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
model.add(Conv2D(16, kernel_size=(3, 3), activation="relu", strides=(1, 1), padding="same"))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
model.add(Flatten())
model.add(Dense(120, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(num_classes, activation="softmax"))


if __name__ == "__main__":
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.summary()

    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1)
    score = model.evaluate(X_test, y_test)
    print(f"Test loss: {score[0]}")
    print(f"Test accuracy: {score[1]}")

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
    tflite_model = converter.convert()
    tflite_model_name = "cnn_model"
    c_model_name = "cnn_model_c"
    open(tflite_model_name + ".tflite", "wb").write(tflite_model)
    with open(c_model_name + ".h", "w") as file:
        file.write(hex_to_c_array(tflite_model, c_model_name))






