import random as rnd

x0 = rnd.randint(-100, 100)


def f(x):
    return 2 * x**7 + 5 * x + 2


def fP(x):
    return 14 * x**6 + 5


def main(x0):
    while True:
        x1 = x0 - (f(x0) / fP(x0))

        if f(x0) == 0:
            print(x1)
            break
        else:
            x0 = x1


if __name__ == "__main__":
    main(x0)
