import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


def plot_mic_output(df):
    mics = ["Front Left", "Front Right", "Back Left", "Back Right"]
    colors = ["r", "b", "g", "orange"]
    plt.figure(figsize=(16, 16))
    for i in range(df.shape[0]):
        plt.plot(range(0, df.shape[1]), df[i, :], label=f"{mics[i]} Microphone", color=colors[i])
    plt.xlabel("Sample", fontsize=18)
    plt.xticks(fontsize=16)
    plt.ylabel("Voltagte (mv)", fontsize=18)
    plt.yticks(fontsize=16)
    plt.title(f"Data sample taken with a frequency sweep", fontsize=20)
    plt.legend(loc="lower right", fontsize=16)
    plt.grid()
    plt.autoscale(enable=True, axis="x", tight=True)
    plt.savefig(".".join((data_path.split("/")[-1]).split(".")[:-1]) + ".jpg")
    plt.close()


if __name__ == "__main__":
    data_path = "../../utils/data/audio/1_0.553_2.870_0.csv"
    df = pd.read_csv(data_path, header=None).values[:, 1:]
    plot_mic_output(df)

