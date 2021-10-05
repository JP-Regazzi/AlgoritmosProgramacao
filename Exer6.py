def matriz3x3(a):
    positivo = (a[0][0] * a[1][1] * a[2][2]) + (a[0][1] * a[1][2] * a[2][0]) + (a[0][2] * a[1][0] * a[2][1])
    negativo = ((a[0][0]*a[1][2]*a[2][1]) + (a[0][1]*a[1][0]*a[2][2]) + (a[0][2]*a[1][1]*a[2][0]))
    return positivo - negativo


def matriz4x4(b):
    resultado = 0
    copia_coluna = []
    for w in range(len(b)):  # Copio c primeira coluna
        copia_coluna += [b[w][0]]
    for x in range(len(b)):  # Removo c primeira coluna
        b[x].pop(0)
    for posicao, y in enumerate(copia_coluna):
        c = []
        for n_linha in range(len(b)):  # Crio uma copia da matriz original
            linha = b[n_linha].copy()
            c.append(linha)
        c.pop(posicao)  # Removo uma linha da copia de b (c)
        if len(c) == 3:
            if posicao % 2 != 0:
                resultado -= y * matriz3x3(c)
            else:
                resultado += y * matriz3x3(c)
        else:
            if posicao % 2 != 0:
                resultado -= y * matriz4x4(c)
            else:
                resultado += y * matriz4x4(c)
    return resultado


matriz_inicial = eval(input(''))
if len(matriz_inicial) == 3:
    print((matriz3x3(matriz_inicial)))
else:
    print(matriz4x4(matriz_inicial))
