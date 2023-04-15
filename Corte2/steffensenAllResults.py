import random as rnd
import re


def getEq():
    eQ = "3*xI**2 - 2*xI - 1 "

    match = re.search(r"\*\*?\s*(\d+)", str(eQ))

    if match:
        degree = int(match.group(1))
    else:
        degree = 1

    if (degree % 2) == 0:
        eQ = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eQ)

    return eQ, degree


def getSeed(roots):
    while True:
        x0 = rnd.uniform(-10, 10)
        if x0 not in roots:
            return x0


def cleanArray(arr, margin):
    return sorted(
        [arr[0]]
        + [arr[i] for i in range(1, len(arr)) if abs(arr[i] - arr[i - 1]) > margin]
    )


def verifyRoots(roots, num, count):
    if round(num, 2) not in roots:
        print(f"X = {num}  Count = {count}")
        roots.append(round(num, 2))


def main():
    roots = []
    eQ, degree = getEq()
    bigCount = 0

    while len(roots) < degree:
        bigCount += 1
        count = 0
        x0 = getSeed(roots)

        while True:
            count += 1

            eqX0 = eQ.replace("xI", str(x0))

            if abs(eval(eqX0)) <= 0.00001:
                verifyRoots(roots, x0, count)
                break
            else:
                eqX0PlusEqX0 = eQ.replace("xI", str(x0 + eval(eqX0)))

                x1 = x0 - ((eval(eqX0) ** 2) / (eval(eqX0PlusEqX0) - eval(eqX0)))

                eqX1 = eQ.replace("xI", str(x1))

                if abs(eval(eqX1)) <= 0.00001:
                    verifyRoots(roots, x1, count)
                    break
                else:
                    x0 = x1

                if count > 1000:
                    break
        if bigCount > 100:
            break

    roots = cleanArray(roots, 0.1)
    print(roots)


if __name__ == "__main__":
    main()
