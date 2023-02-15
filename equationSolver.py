import random as rnd

xI = rnd.randint(-100, 100)


# (3 * xI) - 27 = 9
# (5 * xI) - 15 = 3
# 3 * ((2 * xI) + 1) + 9 = -2


def equation(xI):
    return 3 * ((2 * xI) + 1) + 9


# La ecuación siempre tiene que dar 0
if abs(equation(xI)) <= 0.001:
    print(f"Felicidades, llegaste a la respuesta, es: {xI}")

else:
    counter = 0
    while True:
        counter = counter + 1

        res = equation(xI)

        if res > 0:
            x1 = xI - 0.2
            xI = x1
        else:
            x2 = xI + 0.2
            xI = x2

        if equation(round(xI)) == 0:
            print(
                f"Felicidades, llegaste a la respuesta, es: {round(xI)} y el número de iteraciones fue: {counter}"
            )
            break
