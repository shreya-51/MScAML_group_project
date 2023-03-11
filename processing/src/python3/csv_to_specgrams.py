import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import pandas as pd
import os


def convert_to_spectrograms(path_data, Fs=65536, T=0.0005):
    paths = os.listdir(path_data)
    n_fft = int(Fs*T)

    for path in paths:
        df = pd.read_csv(path_data + path)
        mic_outs = df.values
        name = (path.split("/")[-1]).split(".")[0]
        for i in range(mic_outs.shape[0]):
            mic_out = mic_outs[i, :]
            fig = plt.figure(figsize=(12,12), frameon=False)
            fig.set_size_inches(12, 12)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            ax.set_aspect("auto")
            plt.specgram(mic_out, NFFT=n_fft, Fs=Fs, noverlap=int(n_fft/10))
            plt.savefig(f"data_converted/{name}_micro_{i}_spectrogram.jpg", bbox_inches="tight")
    return


path = "/Users/matt/Documents/Imperial College London/Modules/Applied Machine Learning Group Project/MScAML_group_project/processing/src/python3/data/"
convert_to_spectrograms(path)



