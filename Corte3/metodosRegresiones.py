import random as rnd
import numpy as np
import matplotlib.pyplot as plt


def linearInterpolation(arrX, arrY):
    rndI1 = rnd.randint(0, len(arrX) - 1)

    while True:
        rnd2 = rnd.randint(0, len(arrX) - 1)
        if rnd2 != rndI1:
            break

    m = (arrY[rnd2] - arrY[rndI1]) / (arrX[rnd2] - arrX[rndI1])
    b = arrY[rndI1] - m * arrX[rndI1]

    print(f"Linear Interpolation (blue): {m} * x + {b}")
    f = m * arrX + b

    return f


def minimumSquares(arrX, arrY):
    n = len(arrX)
    m = ((n * np.sum(arrX * arrY)) - (np.sum(arrX) * np.sum(arrY))) / (
        (n * np.sum(arrX**2)) - (np.sum(arrX) ** 2)
    )
    b = ((np.sum(arrX) * np.sum(arrX * arrY)) - (np.sum(arrY) * np.sum(arrX**2))) / (
        (np.sum(arrX) ** 2) - (n * np.sum(arrX**2))
    )

    print(f"Minimum Squares (green): {m} * x + {b}")
    f = m * arrX + b

    return f


def variance(arrX, arrY):
    cov = np.cov(arrX, arrY)[0, 1]
    varX = np.var(arrX)

    m = cov / varX
    b = np.mean(arrY) - (m * np.mean(arrX))

    print(f"Variance (red): {m} * x + {b}")
    f = m * arrX + b

    return f


# Place for data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([21, 35, 57, 87, 125, 171, 225, 287])
# Graphs
plt.plot(X, linearInterpolation(X, Y), "-b", label="Linear Interpolation")
plt.plot(X, minimumSquares(X, Y), "-g", label="Minimum Squares")
plt.plot(X, variance(X, Y), "-r", label="Variance")
plt.plot(X, Y, ".k", label="Data")
plt.legend()
plt.show()
