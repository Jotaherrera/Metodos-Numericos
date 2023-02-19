import random as rnd

count = 0

# (3 * xI) - 27 = 9
# (5 * xI) - 15 = 3
# 3 * ((2 * xI) + 1) + 9 = -2


def eq(xI):
    return 3 * ((2 * xI) + 1) + 9


def rndNumbers():
    xLow = rnd.randint(-100, 100)
    xHigh = rnd.randint(xLow, 100)

    return xLow, xHigh


def biseccion(xLow, xHigh):
    global count
    count = count + 1
    if xHigh >= xLow:
        xMiddle = (xHigh + xLow) // 2

        res = eq(xMiddle)

        if res == 0:
            isInList = 1
            return xMiddle, count, isInList
        elif res > 0:
            return biseccion(xLow, xMiddle - 1)
        else:
            return biseccion(xMiddle + 1, xHigh)
    else:
        isInList = 0
        print(f"El elemento no estaba presente en el rango, generando uno nuevo... ")
        return 0, count, 0


isInList = 0

while isInList == 0:
    xLow, xHigh = rndNumbers()
    x, count, isInList = biseccion(xLow, xHigh)

print(f"La X de la ecuación corresponde a {x} y el número de iteraciones fue {count}")
