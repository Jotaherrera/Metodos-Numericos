import random as rnd


def f(xI):
    return 2 * xI**3 - 8 * xI**2 + 5 * xI - 2


def rndNumbers():
    xLow = rnd.randint(-10, 10)
    while f(xLow) > 0:
        xLow = rnd.randint(-10, 10)

    xHigh = rnd.randint(xLow, 10)
    while f(xHigh) < 0:
        xHigh = rnd.randint(xLow, 10)

    print(f"* El rango de búsqueda es de {xLow} a {xHigh} ")
    return xLow, xHigh


def pFP(xLow, xHigh):
    return (f(xLow) - f(xHigh)) / (xLow - xHigh)


count = 0

xLow, xHigh = rndNumbers()

while True:
    count += 1

    x = pFP(xLow, xHigh)

    xC = xLow - (f(xLow) / pFP(x, xHigh))

    if f(xC) == 0:
        print(f"Ok {xC}")
        break
    else:
        xLow = xC
