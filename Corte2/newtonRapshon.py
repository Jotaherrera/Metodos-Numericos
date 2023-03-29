import random as rnd

x0 = rnd.randint(-1000, 1000)


def f(xI):
    return xI**3 + 3 * xI**2 + 3 * xI + 1


def fP(xI):
    return 3 * xI**2 + 6 * xI + 3


def main(x0):
    count = 0
    while True:
        count += 1
        x1 = x0 - (f(x0) / fP(x0))

        if f(x0) == 0:
            print(f"X = {round(x1, 2)}  Count = {count}")
            break
        else:
            x0 = x1


if __name__ == "__main__":
    main(x0)
