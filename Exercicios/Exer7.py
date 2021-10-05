A = eval(input())
B = eval(input())


def elementos_iguais(a, b):
    if a == [] or b == []:
        return False
    elif a[0] == b[0]:
        return True
    else:
        a.pop(0)
        b.pop(0)
        return elementos_iguais(a, b)


print(elementos_iguais(A, B))
