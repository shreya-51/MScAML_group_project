import serial
import matplotlib.pyplot as plt
import time 
import cv2
import numpy as np
import pandas as pd


def sample_data_from_arduino(usb_port, num_mics, sampling_rate=65536):
    ser = serial.Serial(usb_port, 9600, timeout=1)
    array = np.empty((1, num_mics))
    start_time = time.time()
    num_data = []
    sample = 0
    while True:
        # Read a line of data from the serial port
        data = ser.readline().decode("utf-8")
        data = data.split(" ")
        if start_time >= 1/sampling_rate:
            num_data = np.expand_dims(np.array([int(data[i]) for i in range(len(data) - 1)]), axis=0)
            array = np.append(array, num_data, axis=0)
            start_time = time.time()
            sample += 1

        if sample >= 1000:
            filename = input("Enter the csv filename: ")
            structured_array = array.T
            df = pd.DataFrame(data=structured_array)
            path = "data/" + filename + ".csv"
            df.to_csv(path, index=False, header=False)
            return structured_array

def plot_sampled_data(data):
    plt.figure(figsize=(12, 12))
    plt.plot(range(1, data.shape[1]), data[0, 1:], linewidth=1)
    plt.plot(range(1, data.shape[1]), data[1, 1:], linewidth=1)
    plt.ylabel("Voltage (mV)")
    plt.xlabel("Sample")
    plt.grid()
    plt.show()
    plt.close()


if __name__ == "__main__":
    usb_port = "/dev/cu.usbmodem1101" # change if the name is different
    num_mics = 2
    sampling_rate = 65536 # Hz
    data = sample_data_from_arduino(usb_port, num_mics, sampling_rate)
    plot_sampled_data(data)

