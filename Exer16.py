# Questao 5 da prova
n = int(input())


def eprimo(x):
    if x < 2:
        return False
    for numero in range(2, x):
        if x % numero == 0:
            return False
    return True


def rotacionador(x):
    lista_x = list(str(x))
    lista_rotacionados = []
    for i in range(len(lista_x)):
        ultimo = lista_x.pop()
        lista_x.insert(0, ultimo)
        num_rotacionado = ''.join(lista_x)
        lista_rotacionados.append(num_rotacionado)
    return lista_rotacionados


def primoscirculares(n):
    lista_primos_circulares = []
    for numero in range(n+1):
        primo_circular = True
        if eprimo(numero):
            if len(str(numero)) == 1:
                lista_primos_circulares.append(numero)
            else:
                for numero_rotacionado in rotacionador(numero):
                    if not eprimo(int(numero_rotacionado)):
                        primo_circular = False
                if primo_circular:
                    lista_primos_circulares.append(numero)
    return lista_primos_circulares


print(primoscirculares(n))