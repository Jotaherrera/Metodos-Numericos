import matplotlib.pyplot as plt
import numpy as np


def getArtificialData():
    x1_min, x1_max = 0, 5
    x2_min, x2_max = 0, 3
    x1_dim, x2_dim = np.meshgrid(
        np.arange(x1_min, x1_max, 0.1), np.arange(x2_min, x2_max, 0.1)
    )
    X1 = x1_dim.ravel()
    X2 = x2_dim.ravel()
    Y = 2 * X1 + 1.5 * X2 + 3 + np.random.randn(*X1.shape) * 0.3
    return X1, X2, Y


def graph(ax, ax2, X1, X2, Y, m1, m2, b, loss, step, MSE):
    ax.clear()
    ax.scatter(
        X1,
        X2,
        m1 * X1 + m2 * X2 + b + np.random.randn(*X1.shape) * 0.3,
        c="orange",
        label="PC",
    )
    ax.scatter(X1, X2, 2 * X1 + 1.5 * X2 + 3, c="blue", label="Original")
    ax.set_title("Artificial Data")
    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Y")
    ax.set_xlim([0, 5])
    ax.set_ylim([0, 3])
    ax.set_zlim([2.5, 18])
    ax.legend()

    ax2.clear()
    ax2.plot(range(len(loss)), loss, label=f"MSE = {round(MSE, 2)}")
    ax2.set_title("MSE vs Epochs")
    ax2.set_xlabel("Epochs")
    ax2.set_ylabel("MSE")
    ax2.set_xlim([0, 500])
    ax2.set_ylim([0, 5])
    ax2.legend()

    plt.tight_layout()
    plt.draw()
    plt.pause(1)


def main():
    X1, X2, Y = getArtificialData()

    b, m1, m2 = np.random.randint(0, 5, size=3)
    display_step = 50
    N = len(X1)
    loss = []
    epochs = 500
    learning_rate = 0.01
    convergence_criteria = 1e-5

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(121, projection="3d")
    ax2 = fig.add_subplot(122)
    plt.ion()

    for step in range(epochs):
        m1_gradient = 0
        m2_gradient = 0
        b_gradient = 0
        error = 0

        for i in range(N):
            Yp = m1 * X1[i] + m2 * X2[i] + b
            dif = Yp - Y[i]
            error += dif**2
            m1_gradient += (2 / N) * dif * X1[i]
            m2_gradient += (2 / N) * dif * X2[i]
            b_gradient += (2 / N) * dif * 1

        MSE = error / N
        m1 -= m1_gradient * learning_rate
        m2 -= m2_gradient * learning_rate
        b -= b_gradient * learning_rate

        loss.append(np.abs(MSE))

        if step % display_step == 0:
            graph(ax, ax2, X1, X2, Y, m1, m2, b, loss, step, MSE)

        if (
            max(abs(learning_rate * m1_gradient), abs(learning_rate * b_gradient))
            < convergence_criteria
        ):
            break

    print(f"Y = {m1}x1 + {m2}x2 + {b}")
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
