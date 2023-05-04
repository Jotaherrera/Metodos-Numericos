import random as rnd
from sympy import *
import re


def getEntry():
    # Get equation from entry box
    rawEq = "3*x**2 - 2*x - 1"
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


def getEntryRaw():
    rawEq = "3*x**2 - 2*x - 1"
    # Change x for xI
    eqVar = rawEq.replace("x", "xI").replace("X", "xI")

    return eqVar


def getIntSeed(roots):
    while True:
        x0 = rnd.randint(-10, 10)
        if x0 not in roots:
            return x0


def verifyRoots(roots, counters, num, count):
    if round(num, 2) not in roots:
        roots.append(round(num, 2))
        counters.append(count)


def cleanArray(arr, margin):
    return sorted(
        [arr[0]]
        + [arr[i] for i in range(1, len(arr)) if abs(arr[i] - arr[i - 1]) > margin]
    )


def getDerivative():
    eqVarRaw = getEntryRaw()
    x = symbols("xI")
    sympify(eqVarRaw)
    derivative = diff(eqVarRaw, x)
    derivativeString = str(derivative)
    return derivativeString


def newtonRaphson():
    roots = []
    counters = []
    bigCount = 0
    eqVar, degree = getEntry()
    eqDerivative = getDerivative()
    while len(roots) < degree:
        bigCount += 1
        counter = 0
        x0 = getIntSeed(roots)

        while True:
            counter += 1

            if (eval(eqVar, {"xI": x0})) == 0:
                verifyRoots(roots, counters, x0, counter)
                break
            if (eval(eqDerivative, {"xI": x0})) == 0:
                verifyRoots(roots, counters, x1, counter)
                break

            x1 = x0 - ((eval(eqVar, {"xI": x0})) / (eval(eqDerivative, {"xI": x0})))

            if (eval(eqVar, {"xI": x0})) == 0:
                verifyRoots(roots, counters, x1, counter)
                break
            else:
                x0 = x1

            if counter > 10000:
                if len(roots) == 0:
                    # messagebox.showinfo(
                    #     title="Bisección",
                    #     message="Se supero el número de iteraciones por Bisección, no se pudo resolver por este método.",
                    # )
                    return roots
                break
        if bigCount > 500:
            break
    roots = cleanArray(roots, 0.1)
    # self.giveAnswers(
    #     self.biseccionOutput, self.biseccionIterationsOutput, roots, counters
    # )

    return roots


print(newtonRaphson())
