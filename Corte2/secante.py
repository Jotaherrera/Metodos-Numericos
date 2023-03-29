import random as rnd


def f(xI):
    return xI**3 + 3 * xI**2 + 3 * xI + 1


def rndNumbers():
    xLow = rnd.randint(-1000, 1000)
    while f(xLow) > 0:
        xLow = rnd.randint(-1000, 1000)

    xHigh = rnd.randint(-1000, 1000)
    while f(xHigh) < 0:
        xHigh = rnd.randint(-1000, 1000)

    print(f"* El rango de búsqueda es de {xLow} a {xHigh} ")
    return xLow, xHigh


def main():
    count = 0

    xLow, xHigh = rndNumbers()

    while True:
        count += 1

        xC = xLow - ((f(xLow) * (xLow - xHigh)) / ((f(xLow) - f(xHigh))))

        if abs(f(xC)) <= 0.0001:
            print(f"X = {round(xC, 2)}  Count = {count}")
            break
        elif f(xLow) * f(xC) < 0:
            xHigh = xC
            xC = xLow - ((f(xLow) * (xLow - xHigh)) / (f(xLow) - f(xHigh)))
        else:
            xLow = xC
            xC = xLow - ((f(xLow) * (xLow - xHigh)) / (f(xLow) - f(xHigh)))


if __name__ == "__main__":
    main()
