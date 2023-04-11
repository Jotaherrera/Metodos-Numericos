import random as rnd

x0 = rnd.randint(-100, 100)


def f(xI):
    return 2 * xI - 8


def main(x0):
    count = 0
    while True:
        count += 1
        x1 = x0 - ((f(x0) ** 2) / (f(x0 + f(x0)) - f(x0)))

        if abs(f(x1)) <= 0.001:
            print(f"X = {round(x1, 2)}  Count = {count}")
            break
        else:
            x0 = x1


if __name__ == "__main__":
    main(x0)
