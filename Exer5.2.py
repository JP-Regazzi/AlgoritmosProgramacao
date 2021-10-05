matriz_inicial = eval(input('Digite uma matriz quadrada'))
n = len(matriz_inicial)


def matriz1x1(c):
    return c[0]


def matriz2x2(b):
    return (b[0][0] * b[1][1]) - b[0][1] * b[1][0]


def matriz3x3(a):
    positivo = (a[0][0] * a[1][1] * a[2][2]) + (a[0][1] * a[1][2] * a[2][0]) + (a[0][2] * a[1][0] * a[2][1])
    negativo = ((a[0][0]*a[1][2]*a[2][1]) + (a[0][1]*a[1][0]*a[2][2]) + (a[0][2]*a[1][1]*a[2][0]))
    return positivo - negativo


if n == 1:
    print(matriz1x1(matriz_inicial))
elif n == 2:
    print(matriz2x2(matriz_inicial))
else:
    print(matriz3x3(matriz_inicial))
