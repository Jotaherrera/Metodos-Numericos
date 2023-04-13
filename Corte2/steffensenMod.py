import random as rnd
import re


def equation():
    eQ = "xI**3 - 5*xI**2 + 8*xI - 4"

    match = re.search(r"\*\*?\s*(\d+)", str(eQ))

    if match:
        degree = int(match.group(1))
    else:
        degree = 1

    if (degree % 2) == 0:
        eQ = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eQ)
    return eQ, degree


def main():
    roots = []

    eQ, degree = equation()

    while len(roots) < degree:
        count = 0
        x0 = rnd.randint(-10, 10)
        while x0 in roots:
            x0 = rnd.randint(-10, 10)

        while True:
            count += 1

            eqX0 = eQ.replace("xI", str(x0))
            eqX0PlusEqX0 = eQ.replace("xI", str(x0 + eval(eqX0)))

            deno = eval(eqX0PlusEqX0) - eval(eqX0)

            if deno == 0:
                if round(x0, 2) in roots:
                    break
                if count > 1000:
                    break
                print(f"X = {x0}  Count = {count}")
                roots.append(x0)
                break
            else:
                x1 = x0 - ((eval(eqX0) ** 2) / (eval(eqX0PlusEqX0) - eval(eqX0)))

                eqX1 = eQ.replace("xI", str(x1))

                if abs(eval(eqX1)) <= 0.000001:
                    if round(x1, 2) in roots:
                        break
                    print(f"X = {round(x1, 5)}  Count = {count}")
                    roots.append(round(x1, 5))
                    break
                else:
                    x0 = x1

                if count > 1000:
                    break

    print(sorted(set(roots)))


if __name__ == "__main__":
    main()
