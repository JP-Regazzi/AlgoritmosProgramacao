matriz = eval(input())


def verificador_de_quadrado_magico(m):
    tamanho = len(m)
    if tamanho == 1:  # retorna True se a matriz for 1x1
        return True

    soma_referencia = 0  # calcula a soma referencia
    for i in m[0]:
        soma_referencia += i

    for linha in m:  # calcula a soma de todas as linhas separadamente
        soma_linha = 0
        for item_linha in linha:
            soma_linha += item_linha
        if soma_linha != soma_referencia:
            return False

    for coluna in range(tamanho):  # calcula a soma de todas as colunas separadamente
        soma_coluna = 0
        for linha in range(tamanho):  # varia a linha a ser utilizada
            soma_coluna += m[linha][coluna]
        if soma_coluna != soma_referencia:
            return False

    soma_diagonal_p = 0  # calcula a soma da diagonal principal
    for linha_coluna in range(tamanho):
        soma_diagonal_p += m[linha_coluna][linha_coluna]
    if soma_diagonal_p != soma_referencia:
        return False

    soma_diagonal_s = 0  # calcula a soma da diagonal secundaria
    for linha, coluna in zip(range(tamanho), range(-1, -tamanho - 1, -1)):
        soma_diagonal_s += m[linha][coluna]
    if soma_diagonal_s != soma_referencia:
        return False
    return True


print(verificador_de_quadrado_magico(matriz))
