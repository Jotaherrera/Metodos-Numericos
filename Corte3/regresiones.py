import numpy as np
import matplotlib.pyplot as plt

X = np.array(
    [
        0,
        500,
        1000,
        1500,
        2000,
        2500,
        3000,
        3500,
        4000,
        4500,
        5000,
        6000,
        7000,
        8000,
        9000,
        10000,
        11000,
        12000,
        13000,
        14000,
        15000,
    ]
)
Y = np.array(
    [
        1.225,
        1.167,
        1.112,
        1.058,
        1.006,
        0.957,
        0.909,
        0.863,
        0.819,
        0.777,
        0.736,
        0.660,
        0.590,
        0.526,
        0.467,
        0.413,
        0.365,
        0.312,
        0.268,
        0.226,
        0.195,
    ]
)
Y_N = -0.000070 * X + 1.225  # Modelo Y=-0.00007X+1.225
n = len(X)
m = ((n * np.sum(X * Y)) - (np.sum(X) * np.sum(Y))) / (
    (n * np.sum(X**2)) - (np.sum(X) ** 2)
)
b = ((np.sum(X) * np.sum(X * Y)) - (np.sum(Y) * np.sum(X**2))) / (
    (np.sum(X) ** 2) - (n * np.sum(X**2))
)
print(f"{m} * x + {b}")
f = m * X + b
plt.plot(X, Y, ":r", X, Y_N, "-b")
plt.plot(X, Y, ":r", f, "-b")
plt.xlabel("Altitude (m)")
plt.ylabel("Air density (Kg/m^3)")
plt.title("Air density as a fuction of the Altitude")
plt.axis([0, 15000, 0, 1.3])
plt.show()
