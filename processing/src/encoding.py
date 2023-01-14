import os
from collections import defaultdict
import numpy as np
from scipy.io.wavfile import read, write


def preprocess(data):
    mean = np.mean(data)
    std = np.std(data)
    return mean, std


