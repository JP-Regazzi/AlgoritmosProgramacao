matriz_inicial = eval(input('Digite uma matriz quadrada'))
n = len(matriz_inicial)


def matriz1x1(a):
    determinante = a[0]
    return determinante


def matriz2x2(a):
    determinante = (a[0][0]*a[1][1]) - a[0][1]*a[1][0]
    return determinante


def matriz3xs3(a):
    determinante = 0
    for i in range(-3, 0):
        c2 = -2
        c3 = -1
        determinante += a[-3][i]*a[-2][c2]*a[-1][c3] - a[-3][i]*a[-2][c3]*a[-1][c2]
        if c3 == -1:
            c3 = -3
        else:
            c3 += 1
        if c2 == -1:
            c2 = -3
        else:
            c2 += 1
    return determinante


if n == 1:
    print(matriz1x1(matriz_inicial))
elif n == 2:
    print(matriz2x2(matriz_inicial))
else:
    print(matriz3xs3(matriz_inicial))
