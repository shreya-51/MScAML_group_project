import numpy as np

a = np.array([[1, 1, 2, 3]])
b = np.array([[2, 3, 4, 5]])

data = np.empty((1, 4))

while data.shape[0] <= 10:
    print(data.shape)
    print(a.shape)
    print(b.shape)
    data = np.append(data, b, axis=0)
    data = np.append(data, a, axis=0)

print(data)
