import random as rnd

xI = rnd.randint(-1000, 1000)

# Ecuaciones para testing:
# (3 * xI) - 27 = 9
# (5 * xI) - 15 = 3
# 3 * ((2 * xI) + 1) + 9 = -2
# Remplazar cualquier ecuación en el return de la función siguiente


def equation(xI):
    return (3 * xI) - 27


# Este algoritmo solo resuelve ecuaciones donde la variable corresponde a un número entero
if abs(equation(xI)) <= 0.001:
    print(f"Felicidades, llegaste a la respuesta, es: {xI}")

else:
    counter = 0
    while True:
        counter = counter + 1

        if equation(xI) > 0:
            x1 = xI - 0.1
            xI = x1
        else:
            x2 = xI + 0.1
            xI = x2

        if abs(equation(xI)) <= 0.001:
            print(
                f"Felicidades, llegaste a la respuesta, es: {round(xI,2)} y el número de iteraciones fue: {counter}"
            )
            break
