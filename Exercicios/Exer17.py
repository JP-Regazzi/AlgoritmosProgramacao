# Questao 6
matriz = eval(input())


def caminho_diagonal(m):
    lista_posicoes = []
    if len(m) == 1:  # Se a matriz possuir apenas uma linha
        if type(m[0]) == int:
            for coluna in m:
                lista_posicoes += coluna
            return lista_posicoes
        else:
            for coluna in m[0]:
                lista_posicoes += coluna
            return lista_posicoes
    else:  # Se a matriz possuir mais de uma linha
        for linha in range(len(m)):  # Cria uma lista com todas as posicoes possiveis do robo
            for coluna in range(len(m[0])):
                lista_posicoes += [tuple((linha, coluna))]
        for i in range(len(m)):  # Se a posicao nao esta vazia, ela e retirada da lista de posicoes
            for j in range(len(m[0])):
                if m[i][j] == 1:
                    lista_posicoes.remove(tuple((i, j)))
        for casa in lista_posicoes[-2::-1]:  # Retira as posicoes que nao estao ligadas a outra casa vazia
            if not (tuple((casa[0], casa[1]+1)) in lista_posicoes or tuple((casa[0]+1, casa[1])) in lista_posicoes):
                lista_posicoes.remove(casa)
        for casa in lista_posicoes[1:]:
            if not (tuple((casa[0], casa[1]-1)) in lista_posicoes or tuple((casa[0]-1, casa[1])) in lista_posicoes):
                lista_posicoes.remove(casa)
        lista_final = [(0, 0)]
        for casa in lista_posicoes:  # cria uma lista final para retornar, possuindo um caminho possivel
            if lista_final[-1] == tuple((casa[0] - 1, casa[1])) or lista_final[-1] == tuple((casa[0], casa[1] - 1)):
                lista_final += casa,
        if len(lista_final) < len(m) + len(m[0]) - 1:
            return False
        else:
            return lista_final


print(caminho_diagonal(matriz))
