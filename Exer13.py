# Questao 2 da prova
numero = input()
i = 1


def fatorLychrel(n):
    global i
    n_invertido = ''
    soma_invertida = ''
    for algarismo in n[::-1]:  # Crio uma variavel com o numero n lido da direita para esquerda
        n_invertido += algarismo
    soma = f'{int(n) + int(n_invertido)}'
    for algarismo in soma[::-1]:  # Crio uma variavel com o numero da soma lido da direita para esquerda
        soma_invertida += algarismo
    if soma == soma_invertida:  # testo se a soma e um palindromo
        return i
    elif i <= 50:  # se
        i += 1
        return fatorLychrel(soma)
    else:
        return -1


print(fatorLychrel(numero))
