import os
from collections import defaultdict
import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
from PIL import Image


def load_spectrograms(img_path, size):
    X = []
    y = []
    img_paths = os.listdir(img_path)
    for path in img_paths:
        label = (((path.split("/"))[-1]).split("_"))[0]
        img = np.asarray((Image.open(img_path + "/" + path).convert('L')).resize(size))
        X.append(img)
        y.append(int(label))
    return np.expand_dims(np.array(X), axis=-1), np.expand_dims(np.array(y), axis=-1)


if __name__ == "__main__":
    img_path = "../../utils/data/img"
    img_width = 32
    img_length  = 32
    X, y = load_spectrograms(img_path, size=(img_width, img_length))

