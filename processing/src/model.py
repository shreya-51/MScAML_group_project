from pandas import Categorical
import tensoflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from keras.losses import categorical_crossentropy

import keras
from .load_data import load_data

sounds_path = "/Users/matt/Desktop/MScAML_group_project/processing/dataset/recordings/"
img_path = "/Users/matt/Desktop/MScAML_group_project/processing/img_dataset/"
random_state = 1
num_classes = 10
epochs = 1
batch_size = 32

X, y = load_data(sounds_path, img_path)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=random_state)

input_shape = X_train[0].shape

# LeNet-5 model
model = Sequential()
model.add(Conv2D(6, kernel_size=(5, 5), activation="tanh", strides=(1, 1), input_shape=input_shape, padding="same"))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
model.add(Conv2D(16, kernel_size=(5, 5), activation="tanh", strides=(1, 1), padding="same"))
model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
model.add(Flatten())
model.add(Dense(120, activation="tanh"))
model.add(Dense(64, activation="tanh"))
model.add(Dense(num_classes, activation="softmax"))


if __name__ == "__main__":
    model.compile(optimizer="sgd", loss=categorical_crossentropy, metrics=["accuracy"])
    model.summary()

    model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs)
    score = model.evaluate(X_test, y_test)
    print(score)

