import random as rnd
import re


def f():
    eQ = "xI**4 - 6*xI**3 + 11*xI**2 - 6*xI"
    match = re.search(r"\*\*?\s*(\d+)", str(eQ))

    if match:
        degree = int(match.group(1))
    else:
        degree = 0

    if (degree % 2) == 0:
        eQ = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eQ)

    return eQ, degree


def rndNumbers():
    eQ, degree = f()

    xLow = rnd.randint(-10, 10)
    equationLow = eQ.replace("xI", str(xLow))
    while eval(equationLow) > 0:
        xLow = rnd.randint(-100, 100)
        equationLow = eQ.replace("xI", str(xLow))

    xHigh = rnd.randint(xLow, 100)

    equationHigh = eQ.replace("xI", str(xHigh))
    while eval(equationHigh) < 0:
        xHigh = rnd.randint(xLow, 100)
        equationHigh = eQ.replace("xI", str(xHigh))
    return xLow, xHigh


def main():
    eQ, degree = f()
    roots = []
    count = 0
    xC = 0
    maxIterations = 1000

    while len(roots) < degree:
        xLow, xHigh = rndNumbers()

        if xLow >= xHigh:
            break

        if abs(xC) >= abs(xHigh):
            break

        try:
            while True:
                count += 1

                equationLow = eQ.replace("xI", str(xLow))
                equationHigh = eQ.replace("xI", str(xHigh))

                if (eval(equationLow) - eval(equationHigh)) == 0:
                    break

                xC = xLow - (
                    (eval(equationLow) * (xLow - xHigh))
                    / ((eval(equationLow) - eval(equationHigh)))
                )

                eqVar = eQ.replace("xI", str(xC))

                if abs(eval(eqVar)) <= 0.0001 and xC not in roots:
                    print(f"X = {round(xC, 2)}  Count = {count}")

                    roots.append(round(xC, 2))
                    break
                elif eval(equationLow) * eval(eqVar) < 0:
                    xHigh = xC
                    xC = xLow - (
                        (eval(equationLow) * (xLow - xHigh))
                        / (eval(equationLow) - eval(equationHigh))
                    )
                else:
                    xLow = xC
                    xC = xLow - (
                        (eval(equationLow) * (xLow - xHigh))
                        / (eval(equationLow) - eval(equationHigh))
                    )

                if count > maxIterations:
                    break
        except ZeroDivisionError:
            break
    print(sorted(roots))


if __name__ == "__main__":
    main()
