import random as rnd
import re


def evaluateFunction(function, variables, values):
    # """This function creates a dictionary
    # making a relation between the variables
    # and the random values

    # Args:
    #     function (string): current evaluating equation
    #     variables (arr[string]): variables of the equation
    #     values (arr[int]): possible values to check

    # Returns:
    #     int: evaluation of the values in the variables for the equation
    # """
    variablesDict = {}
    for i in range(len(variables)):
        variablesDict[variables[i]] = values[i]
    return eval(function, variablesDict)


def extractInd(arr):
    terms = []
    for i, eq in enumerate(arr):
        regex = r"=\s*([-+]?\d*\.?\d+)"
        indTerm = re.findall(regex, eq)
        arr[i] = eq.split("=")[0].strip()
        terms.append(float(indTerm[0]))
    return terms


def extractVars(arr):
    vars = []
    for item in arr:
        vars += re.findall(r"[a-zA-Z]+", item)
    uniqueVars = []
    for var in vars:
        if var not in uniqueVars:
            uniqueVars.append(var)
    return uniqueVars


def main():
    varNumbers = input("¿Cuantas incógnitas desea despejar?\n   ")
    equations = [
        input(f"Ingrese la ecuación {i + 1}:\n   ") for i in range(int(varNumbers))
    ]
    terms = extractInd(equations)
    vars = extractVars(equations)
    print(
        f"Ecuaciones: {equations}\n Términos independientes: {terms}\n Incógnitas: {vars}\n"
    )

    counter = 0

    while True:
        counter += 1
        rndValues = [rnd.randint(-20, 20) for _ in range(len(vars))]
        allCorrect = all(
            evaluateFunction(f, vars, rndValues) == t for f, t in zip(equations, terms)
        )
        if allCorrect:
            solution = ", ".join(
                [f"{var} = {val}" for var, val in zip(vars, rndValues)]
            )
            print(f"{solution}, iteraciones = {counter}")
            break


if __name__ == "__main__":
    main()
