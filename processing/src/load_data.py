import os
from collections import defaultdict
import numpy as np
from scipy.io.wavfile import read, write
from .encoding import preprocess


def load_data(root_path):
    paths = os.listdir(root_path)
    y = []
    X = []

    for path in paths:
        sound_path = sounds_path + path
        label = (path.split("_"))[0]
        rate, sound = read(sound_path)
        mean, std = preprocess(sound)
        y.append(int(label))
        X.append([mean, std])

    # To return X, we have to preprocess it or at least represent it by smth    
    return np.array(X), np.array(y)


if __name__ == "__main__":
    sounds_path = "/Users/matt/Desktop/MScAML_group_project/processing/dataset/recordings/"
    X, y = load_data(sounds_path)
    print(X)
    print(y)

    



