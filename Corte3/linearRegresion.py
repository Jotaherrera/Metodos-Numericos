from IPython.display import clear_output
import matplotlib.pyplot as plt
import random as rnd
import numpy as np


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

fig, axes = plt.subplots(1, 2, figsize=(18, 5))


for step in range(epochs):
    # Gradientes iniciales (Zero gradients)
    m_gradient = 0
    b_gradient = 0
    error = 0
    Diferencia = 0

    # Calculamos el error y con ello, el gradiente
    for i in range(N):
        Yp = m * X_real[i] + b
        Diferencia = Yp - Y_real[i]
        error += (Diferencia) ** 2  # MSE
        # Calculamos el gradiente
        m_gradient += (2 / N) * (Diferencia) * X_real[i]
        b_gradient += (2 / N) * (Diferencia) * 1

    MSE = error / N

    # Actualizamos los valores de acuerdo al gradiente
    m = m - (m_gradient * learning_rate)
    b = b - (b_gradient * learning_rate)

    # Guardamos el objetivo por cada epoca
    loss.append(np.abs(MSE))

    # Mostramos cada display_step epocas
    if step % display_step == 0:
        axes[0].set_xlim(0, 4)
        axes[0].set_ylim(0, 10)
        axes[0].cla()  # Clear the axes
        axes[0].scatter(X_real, Y_real)
        pred_x = [0, max(X_real)]
        pred_y = m * X_real + b
        axes[0].set_title("Epoca: {0}".format(step))
        axes[0].plot(X_real, pred_y, "r")

        # Refresh the figure
        fig.canvas.draw()
        plt.pause(0.1)
        clear_output()

    # Refresh the figure

    # Paramos el algoritmo cuando los hiperparámetros no estén cambiando lo suficiente
    if (
        max(abs(learning_rate * m_gradient), abs(learning_rate * b_gradient))
        < convergence_criteria
    ):
        plt.show()
        break


# =============Impresión de los resultados==========
print("Los valores obtenidos son: ", "m=", m, "y b=", b)
print("Finalizado en ", step, " iteraciones ")
print("")
Y_prediction4 = m * X_real + b
MSE = np.mean(np.square(Y_prediction4 - Y_real))
print("MSE= ", MSE)

axes[1].plot(loss)
axes[1].set_title("Costo (MSE)")
axes[1].set_xlabel("Epochs")
axes[1].set_ylabel("MSE")

plt.show()
