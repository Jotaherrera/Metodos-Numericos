import random as rnd


def f(xI):
    return 2 * xI**3 - 8 * xI**2 + 5 * xI - 2


def rndNumbers():
    xLow = rnd.randint(-1000, 1000)
    while f(xLow) > 0:
        xLow = rnd.randint(-1000, 1000)

    xHigh = rnd.randint(xLow, 1000)
    while f(xHigh) < 0:
        xHigh = rnd.randint(xLow, 1000)

    print(f"* El rango de búsqueda es de {xLow} a {xHigh} ")
    return xLow, xHigh


def main():
    count = 0

    xLow, xHigh = rndNumbers()

    while True:
        count += 1

        xC = xLow - ((f(xLow) * (xLow - xHigh)) / ((f(xLow) - f(xHigh))))

        if abs(f(xC)) <= 0.0001:
            print(f"X = {xC}  Count = {count}")
            break
        elif f(xLow) * f(xC) < 0:
            xHigh = xC
            xC = xLow - ((f(xLow) * (xLow - xHigh)) / (f(xLow) - f(xHigh)))
        else:
            xLow = xC
            xC = xLow - ((f(xLow) * (xLow - xHigh)) / (f(xLow) - f(xHigh)))


if __name__ == "__main__":
    main()
