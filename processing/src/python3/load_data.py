import os
from collections import defaultdict
import numpy as np
from scipy.io.wavfile import read, write
from .encoding import preprocess
import matplotlib.pyplot as plt
from PIL import Image

img_width=32
img_length=32

def load_data(root_path, img_path):
    sound_paths = os.listdir(root_path)
    img_paths = os.listdir(img_path)

    if img_paths is False:
        for path in sound_paths:
            sound_path = sounds_path + path
            rate, sound = read(sound_path)
            sound_name = (path.split("."))[0]
            preprocess(sound, 2*rate, sound_name)
    
    X, y = load_spectrograms(img_paths)
    return np.array(X), np.array(y)


def load_spectrograms(img_paths):
    X = []
    y = []
    for path in img_paths:
        label = (((path.split("/"))[-1]).split("_"))[0]
        img = np.asarray(Image.open(img_path + path))
        img = img.resize(img_length, img_width)
        X.append(img)
        y.append(label)
    
    return X, y


def plot_signal_with_spectrogram(sound, fs):
    plt.figure(figsize=(12,12))

    plot_a = plt.subplot(211)
    plt.specgram(sound, NFFT=1024, Fs=fs, noverlap=900)
    plot_a.set_xlabel('sample rate * time')
    plot_a.set_ylabel('energy')

    plot_b = plt.subplot(212)
    plot_b.plot(sound)
    plot_b.set_xlabel('Time')
    plot_b.set_ylabel('Frequency')
    plt.show()    


if __name__ == "__main__":
    sounds_path = "/Users/matt/Desktop/MScAML_group_project/processing/dataset/recordings/"
    img_path = "/Users/matt/Desktop/MScAML_group_project/processing/img_dataset/"
    X, y = load_data(sounds_path, img_path)
    print(X)
    print(y)

    



