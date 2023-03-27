import random as rnd

xI = rnd.randint(-1000, 1000)


def eq(xI):
    return 2 * xI**2 - 5 * xI + 2


def tanteo():
    xI = rnd.randint(-100, 100)

    count = 0

    if xI >= 0:
        while True:
            if eq(xI) > 0:
                count += 1
                x1 = xI - 0.001
                xI = x1
            elif eq(xI) < 0:
                count += 1
                x1 = xI + 0.001
                xI = x1
            if abs(eq(xI)) <= 0.001:
                print(
                    f"» La X de la ecuación corresponde a {round(xI, 2)} y el número de iteraciones fue {count}"
                )
                break
    else:  # if xI is negative
        while True:
            if eq(xI) > 0:
                count += 1
                x1 = xI + 0.001
                xI = x1
            elif eq(xI) < 0:
                count += 1
                x1 = xI - 0.001
                xI = x1
            if abs(eq(xI)) <= 0.001:
                print(
                    f"» La X de la ecuación corresponde a {round(xI, 2)} y el número de iteraciones fue {count}"
                )
                break


tanteo()
