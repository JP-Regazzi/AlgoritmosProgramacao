a = int(input())
b = int(input())
c = 0


def divisao_inteira(numerador, denominador):
    global c  # Faco c global para ele manter as alteracoes ao recomecar a funcao
    if numerador < denominador:  # ultima parte da funcao a rodar
        return c
    else:
        c += 1
    return divisao_inteira(numerador-denominador, denominador)  # funcao retorna ela mesma


print(divisao_inteira(a, b))
