matriz1 = eval(input())
matriz2 = eval(input())
n_linhas1 = len(matriz1)
n_linhas2 = len(matriz2)
matriz_produto = []
soma_linha = 0
linha2 = 0
coluna2 = 0
voltas = 0
if type(matriz1[0]) == int:
    n_linhas1 = 1
if type(matriz2[0]) == int:
    n_linhas2 = 1
if n_linhas1 == 1 and n_linhas2 == 1:
    soma_linha = matriz1[0] * matriz2[0]
    matriz_produto.append(soma_linha)
    print(matriz_produto)
    quit()
elif n_linhas1 == 1 and n_linhas2 != 1:
    n_colunas2 = len(matriz2[0])
    while coluna2 < n_colunas2:
        for numero in matriz1:
            soma_linha += numero*matriz2[linha2][coluna2]
            linha2 += 1
        matriz_produto.append(soma_linha)
        coluna2 += 1
    print(matriz_produto)
    quit()
# M1 pode ter varias linhas de 1 coluna e M2 se ter 1 linha e varias colunas
elif n_linhas1 != 1 and n_linhas2 == 1:
    n_colunas2 = len(matriz2)
    for linha in matriz1:
        coluna2 = 0
        while coluna2 < n_colunas2:
            for numero in linha:
                soma_linha += numero*matriz2[coluna2]
                matriz_produto.append(soma_linha)
            coluna2 += 1
            soma_linha = 0
elif n_linhas1 > 1 and n_linhas2 > 1:
    n_colunas2 = len(matriz2[0])
    for linha in matriz1:
        linha2 = 0
        coluna2 = 0
        soma_linha = 0
        voltas = 0
        while voltas < n_colunas2:
            voltas += 1
            linha2 = 0
            soma_linha = 0
            for numero in linha:
                soma_linha += numero*matriz2[linha2][coluna2]
                linha2 += 1
            matriz_produto.append(soma_linha)
            coluna2 += 1
x = 0
matriz_resposta = []
coluna_final = 0
for linha_final in range(n_linhas1):
    matriz_resposta.append(0)
    matriz_resposta[linha_final] = list()
    for coluna_final in range(n_colunas2):
        matriz_resposta[linha_final].append(matriz_produto[x])
        x += 1
print(matriz_resposta)
