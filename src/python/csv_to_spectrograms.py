import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import pandas as pd
import os


def convert_audio_to_spectrograms(data_path, out_dir):
    paths = os.listdir(data_path)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
        
    for path in paths:
        df = pd.read_csv(os.path.join(data_path, path))
        mic_outs = df.values
        # removing .csv file type from a path name
        name = path[:-4]
        for i in range(mic_outs.shape[0]):
            mic_out = mic_outs[i, :]
            fig = plt.figure(figsize=(12,12), frameon=False)
            fig.set_size_inches(12, 12)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            ax.set_aspect("auto")
            plt.specgram(mic_out, NFFT=150, Fs=65536, noverlap=100)
            out_path = os.path.join(out_dir, f"{name}.jpg")
            plt.savefig(out_path, bbox_inches="tight")
            plt.close()


if __name__ == "__main__":
    data_path = "../utils/data/audio/"
    out_dir = "../utils/data/img/"
    convert_audio_to_spectrograms(data_path, out_dir)



