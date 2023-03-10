import serial
import matplotlib.pyplot as plt
import time 
import cv2
import numpy as np
import pandas as pd

usb_port = "/dev/cu.usbmodem1101" # change if the name is different
num_mics = 2
sampling_rate = 65536 # Hz
ser = serial.Serial(usb_port, 9600, timeout=1)

array = np.empty((1, num_mics))
start_time = time.time()
num_data = []
sample = 0
while True:
    data = ser.readline().decode("utf-8")  # Read a line of data from the serial port
    data = data.split(" ")
    #k = cv2.waitKey(30)
    if start_time >= 1/sampling_rate:
        num_data = np.expand_dims(np.array([int(data[i]) for i in range(len(data) - 1)]), axis=0)
        array = np.append(array, num_data, axis=0)
        start_time = time.time()
        sample += 1

    if sample >= 1000: # press ESC to exit
        filename = input("Enter the csv filename: ")
        structured_array = array.T
        df = pd.DataFrame(data=structured_array)
        path = "data/" + filename + ".csv"
        df.to_csv(path, index=False, header=False)
        break


plt.figure(figsize=(12, 12))
plt.plot(range(1, structured_array.shape[1]), structured_array[0, 1:], linewidth=1)
plt.plot(range(1, structured_array.shape[1]), structured_array[1, 1:], linewidth=1)
plt.ylabel("Voltage (mV)")
plt.xlabel("Sample")
plt.grid()
plt.show()


