numero = input()


def contador_de_digitos(a):
    a_numerico = int(a)
    if a_numerico >= 0:
        tamanho = len(a)
        return tamanho
    else:
        return None


def inversor_de_numeros(b):
    numero_invertido = 0
    for i, n in enumerate(b):  # multiplico o algarismo mais significativo por 10 elevado ao indice 0
        numero_invertido += int(n) * (10**i)  # para cada algarismo seguinte multiplico por 10 elevado ao indice 0+i
    return numero_invertido


print((contador_de_digitos(numero), inversor_de_numeros(numero)))
