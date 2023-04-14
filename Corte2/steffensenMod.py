import random as rnd
import re


def getEq():
    eQ = "xI**2 - 5*xI + 6"

    match = re.search(r"\*\*?\s*(\d+)", str(eQ))

    if match:
        degree = int(match.group(1))
    else:
        degree = 1

    if (degree % 2) == 0:
        eQ = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eQ)

    return eQ, degree


def getSeed(roots):
    x0 = rnd.randint(-10, 10)
    while x0 in roots:
        x0 = rnd.randint(-10, 10)
    return x0


def clean_array(arr, threshold):
    unique_arr = [arr[0]]
    for i in range(1, len(arr)):
        if abs(arr[i] - unique_arr[-1]) > threshold:
            unique_arr.append(arr[i])
    return unique_arr


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

            eqX0PlusEqX0 = eQ.replace("xI", str(x0 + eval(eqX0)))

            deno = eval(eqX0PlusEqX0) - eval(eqX0)

            if deno == 0:
                print(f"X = {x0}  Count = {count}")
                roots.append(round(x0, 2))
                break
            else:
                x1 = x0 - ((eval(eqX0) ** 2) / deno)

                eqX1 = eQ.replace("xI", str(x1))

                if abs(eval(eqX1)) <= 0.0000001:
                    if round(x1, 2) in roots:
                        break
                    print(f"X = {round(x1, 2)}  Count = {count}")
                    roots.append(round(x1, 2))
                    break
                else:
                    x0 = x1

                if count > 1000:
                    break
        if bigCount > 100:
            break

    roots = clean_array(roots, 0.1)
    print(sorted(set(roots)))


if __name__ == "__main__":
    main()
