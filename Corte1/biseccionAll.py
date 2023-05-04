import random as rnd
import re


def getEntry():
    # Get equation from entry box
    # rawEq = str(self.eqEntry.get())
    rawEq = "2*x**2 -2"
    # Change x for xI
    eqVar = rawEq.replace("x", "xI").replace("X", "xI")

    # Get equation degree
    match = re.search(r"\*\*?\s*(\d+)", str(eqVar))
    if match:
        degree = int(match.group(1))
    else:
        degree = 1

    if (degree % 2) == 0:
        eqVar = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eqVar)

    return eqVar, degree


def cleanArray(arr, margin):
    return sorted(
        [arr[0]]
        + [arr[i] for i in range(1, len(arr)) if abs(arr[i] - arr[i - 1]) > margin]
    )


def verifyRoots(roots, counters, num, count):
    if round(num, 2) not in roots:
        roots.append(round(num, 2))
        counters.append(count)


# Función de definición de pares de números aleatorios dentro de un rango especifico
def rndNumbers(eqVar, roots):
    xLow = rnd.randint(-100, 100)
    while eval(eqVar, {"xI": xLow}) > 0 and xLow not in roots:
        xLow = rnd.randint(-100, 100)

    xHigh = rnd.randint(-100, 100)
    while eval(eqVar, {"xI": xHigh}) < 0 and xHigh not in roots:
        xHigh = rnd.randint(-100, 10)

    return xLow, xHigh


def biseccion():
    roots = []
    counters = []
    bigCount = 0
    eqVar, degree = getEntry()
    while len(roots) < degree:
        bigCount += 1
        counter = 0
        xLow, xHigh = rndNumbers(eqVar, roots)

        while True:
            counter += 1
            xMiddle = (xHigh + xLow) / 2

            eq = eqVar.replace("xI", str(xMiddle))

            if eval(eqVar, {"xI": xMiddle}) > 0:
                xHigh = xMiddle
            else:
                xLow = xMiddle

            if abs(eval(eqVar, {"xI": xMiddle})) <= 0.0001:
                verifyRoots(roots, counters, xMiddle, counter)
                break

            if counter > 1000:
                break
        if bigCount > 200:
            break
    roots = cleanArray(roots, 0.1)

    return roots


print(biseccion())
