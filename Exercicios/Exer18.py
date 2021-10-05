# Questao 7
L = eval(input())


def mesma_soma_algarismos(L):
    if len(L) == 1:
        return True
    lista_somas = []
    for numero in L:
        soma = 0
        for algarismo in str(numero):
            soma += int(algarismo)
        lista_somas += str(soma)
    for resultado in lista_somas:
        if resultado != lista_somas[0]:
            return False
    return True


print(mesma_soma_algarismos(L))
