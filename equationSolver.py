import random as rnd

xI = rnd.randint(-100, 100)


def equation(xI):
    return (3 * xI) - 27


# La ecuación siempre tiene que dar 0
if abs(equation(xI)) <= 0.001:
    print(f"Felicidades, llegaste a la respuesta, es: {xI}")

else:
    counter = 0
    while True:
        counter = counter + 1

        res = abs(equation(xI))

        if res >= 0.0001:
            x1 = xI + 0.2
            xI = x1
        else:
            x2 = xI - 0.2
            xI = x2

        if abs(equation(xI)) <= 0.001:
            print(
                f"Felicidades, llegaste a la respuesta, es: {round(xI)} y el número de iteraciones fue: {counter}"
            )
            break
