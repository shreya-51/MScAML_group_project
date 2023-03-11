import serial
import matplotlib.pyplot as plt
import time 
import cv2
import numpy as np
import pandas as pd

usb_port = "/dev/cu.usbmodem1101" # change if the name is different
num_mics = 4
sampling_rate = 40000 # Hz
ser = serial.Serial(usb_port, 57600, timeout=0.001)

array = np.empty((1, num_mics))
start_time = time.time()
num_data = []
sample = 0
while True:
    #if ser.readline():
        data = ser.readline().decode("utf-8")  # Read a line of data from the serial port
        data = data.split(" ")
        #k = cv2.waitKey(30)
        if len(data) == 5:
            #if start_time >= 1/sampling_rate:
            num_data = np.expand_dims(np.array([int(data[i]) for i in range(len(data) - 1)]), axis=0)
            array = np.append(array, num_data, axis=0)
            sample += 1

            if sample >= 2000: # press ESC to exit
                filename = input("Enter the csv filename: ") # Save the data in the following way: label_class_x_y_theta
                structured_array = array.T
                df = pd.DataFrame(data=structured_array)
                path = "data/" + filename + ".csv"
                df.to_csv(path, index=False, header=False)
                break
        else:
            #print("THE GAME OF THRONES WAS WAY BETTER WITHOUT 8TH SEASON.")
            continue

    #print(f"Time executed: {((time.time() - start_time) * 1000):.3f}")
    #start_time = time.time()


plt.figure(figsize=(12, 12))
plt.plot(range(1, structured_array.shape[1]), structured_array[0, 1:], linewidth=1)
plt.plot(range(1, structured_array.shape[1]), structured_array[1, 1:], linewidth=1)
plt.plot(range(1, structured_array.shape[1]), structured_array[2, 1:], linewidth=1)
plt.plot(range(1, structured_array.shape[1]), structured_array[3, 1:], linewidth=1)
plt.ylabel("Voltage (mV)")
plt.xlabel("Sample")
plt.grid()
plt.savefig(f"/Users/matt/Desktop/Acoustic Room - trials/{filename}.jpg")
plt.show()


