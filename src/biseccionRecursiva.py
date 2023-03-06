import random as rnd


# Función ecuación.
def eq(xI):
    return (3 * xI) - 27


# Función de definición de pares de números aleatorios dentro de un rango especifico
def rndNumbers():
    xLow = rnd.randint(-1000, 1000)
    while eq(xLow) > 0:
        xLow = rnd.randint(-1000, 1000)

    xHigh = rnd.randint(xLow, 1000)
    while eq(xHigh) < 0:
        xHigh = rnd.randint(xLow, 1000)

    print(f"* El rango de búsqueda es de {xLow} a {xHigh} ")
    return xLow, xHigh


# Función recursiva de búsqueda bi-seccionada.
def biseccion(xLow, xHigh, count=0):
    count = count + 1

    xMiddle = (xHigh + xLow) / 2

    if abs(eq(xMiddle)) <= 0.001:
        return xMiddle, count
    elif eq(xMiddle) > 0.001:
        return biseccion(xLow, xMiddle - 0.1, count)
    else:
        return biseccion(xMiddle + 0.1, xHigh, count)


xLow, xHigh = rndNumbers()
x, count = biseccion(xLow, xHigh)

print(
    f"» La X de la ecuación corresponde a {round(x, 2)} y el número de iteraciones fue {count}"
)
