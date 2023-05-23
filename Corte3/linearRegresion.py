import matplotlib.pyplot as plt
import random as rnd
import numpy as np


def main():
    X_real = np.linspace(0, 4, 100)
    Y_real = 2 * X_real + 1 + np.random.randn(*X_real.shape) * 0.2

    m = rnd.randint(0, 5)
    b = rnd.randint(0, 5)

    display_step = 50
    N = len(X_real)
    loss = []

    epochs = 500
    learning_rate = 0.01
    convergence_criteria = 1e-5

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    plt.ion()  # Turn on interactive mode

    for step in range(epochs):
        m_gradient = 0
        b_gradient = 0
        error = 0
        difference = 0

        for i in range(N):
            Yp = m * X_real[i] + b
            difference = Yp - Y_real[i]
            error += difference**2
            m_gradient += (2 / N) * difference * X_real[i]
            b_gradient += (2 / N) * difference * 1

        MSE = error / N

        m -= m_gradient * learning_rate
        b -= b_gradient * learning_rate

        loss.append(np.abs(MSE))

        if step % display_step == 0:
            axes[0].set_xlim(0, 4)
            axes[0].set_ylim(0, 10)
            axes[0].cla()
            axes[0].scatter(X_real, Y_real)
            pred_x = [0, max(X_real)]
            pred_y = m * X_real + b
            axes[0].set_title("Epoch: {0}".format(step))
            axes[0].plot(X_real, pred_y, "r")

            plt.draw()
            plt.pause(0.1)

        if (
            max(abs(learning_rate * m_gradient), abs(learning_rate * b_gradient))
            < convergence_criteria
        ):
            plt.ioff()
            plt.show()
            break

    plt.ioff()

    print("Values: m =", m, "y b =", b)
    print("Finished in", step, "iterations")
    print("")
    Y_prediction = m * X_real + b
    MSE = np.mean(np.square(Y_prediction - Y_real))
    print("MSE =", MSE)

    axes[1].plot(loss)
    axes[1].set_title("Cost (MSE)")
    axes[1].set_xlabel("Epochs")
    axes[1].set_ylabel("MSE")

    plt.show()


if __name__ == "__main__":
    main()
