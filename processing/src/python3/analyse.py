from pickle import NONE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "/Users/matt/Documents/Imperial College London/Modules/Applied Machine Learning Group Project/MScAML_group_project/processing/src/python3/data"

df_room1_close = pd.read_csv(path + "/trial_2_0.56_3.73.csv", header=None)
df_room1_close_reverse = pd.read_csv(path + "/trial_3_0.56_3.73_opp_angle.csv", header=None)
df_room1_very_close = pd.read_csv(path + "/trial_4_0.455_0.407.csv", header=None)



for i in range(df_room1_close.shape[0]):
    print(f"######## Microphone {i + 1} Stats ########")
    print(df_room1_close.iloc[i, :].describe())
    print(df_room1_close_reverse.iloc[i, :].describe())
    print(df_room1_very_close.iloc[i, :].describe())



df_1khz = pd.read_csv("/Users/matt/Documents/Imperial College London/Modules/Applied Machine Learning Group Project/MScAML_group_project/processing/src/python3/data/trial_1kHz_330_degrees.csv", header=None)

arr_1khz = df_1khz.to_numpy()

for i in range(arr_1khz.shape[0]):
    plt.plot(range(800, 1200), arr_1khz[i, 800:1200])
plt.savefig("close.jpg")
plt.show()





