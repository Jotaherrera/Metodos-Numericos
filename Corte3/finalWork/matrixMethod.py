import numpy as np
import matplotlib.pyplot as plt


def graph(X1, X2, Y_real, Y_predict):
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.plot(X1, X2, Y_real, "blue", label="Base Model")
    ax.set_xlim(X1.min(), X1.max())
    ax.set_ylim(X2.min(), X2.max())
    ax.set_zlim(Y_real.min(), Y_real.max())
    plt.legend()

    ax1 = fig.add_subplot(1, 2, 2, projection="3d")
    ax1.plot(X1, X2, Y_predict, "orange", label="Matrix Model")
    ax1.set_xlim(X1.min(), X1.max())
    ax1.set_ylim(X2.min(), X2.max())
    ax1.set_zlim(Y_real.min(), Y_real.max())
    plt.legend()
    plt.show()


def main():
    x, y = np.meshgrid(np.arange(0, 3, 0.1), np.arange(0, 3, 0.1))

    X1 = x.ravel()
    X2 = y.ravel()

    Y_real = 2 * X1 + 1.5 * X2 + 3 + np.random.randn(*X1.shape) * 0.3

    unitaryMatrix = np.ones_like(X1)
    X = np.column_stack((unitaryMatrix, X1, X2))
    coefficients = np.linalg.inv(X.T @ X) @ (X.T @ Y_real)

    Y_predict = coefficients[0] + coefficients[1] * X1 + coefficients[2] * X2

    print(sorted(list(map(lambda x: round(x, 2), coefficients)), reverse=True))

    graph(X1, X2, Y_real, Y_predict)


if __name__ == "__main__":
    main()
