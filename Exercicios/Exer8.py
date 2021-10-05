a = eval(input())
a_copia = a.copy()
b = eval(input())
c = []


def verificador_de_subsequencia(x, y):
    if x == [] or y == []:  # Ultimo if a rodar na funcao
        return c
    elif x[0] == y[0]:  # Adiciona o valor x[0] em c e deleta os valores x[0] e y[0]
        c.append(x[0])
        x.pop(0)
        y.pop(0)
        return verificador_de_subsequencia(x, y)
    else:  # Se x[0] != de y[0] deleta-se y[0] e chama a funcao novamente
        y.pop(0)
        return verificador_de_subsequencia(x, y)


if a_copia == verificador_de_subsequencia(a, b):  # Se o valor origianl de a (a_copia) foi igual a c (retorno da funcao)
    print(True)  # Imprime True
else:  # se a_copia != c, imprime False
    print(False)


