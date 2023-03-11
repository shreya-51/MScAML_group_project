import numpy as np
import pandas as pd
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/matt/Documents/Imperial College London/Modules/Applied Machine Learning Group Project/MScAML_group_project/processing/src/python3/data/lol2.csv", header=None)

mic_data = df.to_numpy()

mic_1 = mic_data[0, :]
SAMPLE_RATE = 1000
DURATION = 7
N = SAMPLE_RATE * DURATION
mic_1_freq = fft(mic_1)
xf = fftfreq(N + 1, 1/0.001)

plt.plot(xf, abs(mic_1_freq))
plt.show()
