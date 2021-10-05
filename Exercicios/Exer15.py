# Questao 4 da prova
a, b = input(), input()


def anagrama(a, b):
    lista_b = list(b)
    if len(a) != len(b):
        return False
    for caracter_a in a:
        print(lista_b)
        for caracter_b in lista_b:
            if caracter_a == caracter_b:
                lista_b.remove(caracter_b)
                break
    if lista_b == []:
        return True
    else:
        return False


print(anagrama(a, b))







