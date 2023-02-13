import os
from collections import defaultdict
import numpy as np
from scipy.io.wavfile import read, write
from scipy.signal import spectrogram
import pylab

root = "/Users/matt/Desktop/MScAML_group_project/processing/img_dataset/"
def preprocess(data, data_rate, sound_name):
    pylab.specgram(data, Fs=data_rate)
    pylab.savefig(root + sound_name + ".jpg")


