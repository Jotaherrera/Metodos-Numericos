import random as rnd
import sys as sys

sys.setrecursionlimit(10**6)

# Ecuaciones de prueba, remplazar en el return de la función siguiente
# (3 * xI) - 27 = 9
# (5 * xI) - 15 = 3
# 3 * ((2 * xI) + 1) + 9 = -2


# Función ecuación.
def eq(xI):
    return (2 * xI) - 11


# Función de definición de pares de números aleatorios dentro de un rango especifico
def rndNumbers():
    # Se pude revisar si esta por encima de 0 o por debajo desde aca
    xLow = rnd.randint(-100, 100)
    xHigh = rnd.randint(xLow, 100)

    print(f"* El rango de búsqueda es de {xLow} a {xHigh} ")
    return xLow, xHigh


count = 0


# Función recursiva de búsqueda bi-seccionada.
def biseccion(xLow, xHigh):
    global count
    count = count + 1

    if xHigh >= xLow:
        xMiddle = (xHigh + xLow) / 2

        res = eq(xMiddle)

        if abs(res) == 0:
            isInList = 1
            return xMiddle, count, isInList
        elif abs(res) >= 0.001:
            return biseccion(xLow, xMiddle - 0.1)
        else:
            return biseccion(xMiddle + 0.1, xHigh)
    else:
        # Cuando el número menor sobrepasa el mayor el resultado
        # no se encuentra dentro de ese rango,por lo que se genera uno nuevo.
        isInList = 0
        print(f"Χ El elemento no estaba presente en el rango, generando uno nuevo... ")
        return 0, count, 0


isInList = 0

# Ciclo de ejecución de ambas funciones hasta que la función principal
# devuelva el resultado correcto.
while isInList == 0:
    xLow, xHigh = rndNumbers()
    x, count, isInList = biseccion(xLow, xHigh)

print(f"» La X de la ecuación corresponde a {x} y el número de iteraciones fue {count}")
