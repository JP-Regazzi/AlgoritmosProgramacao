# Questao 1 da prova
L = eval(input())
I = int(input())


def particiona(l, i):
    global L
    l_nova = []
    x = l[i]
    for algarismo in l:  # Adiciona todos os algarismos menores que x em uma lista nova e os remove da original
        if algarismo < x:
            l_nova.append(algarismo)
            l.remove(algarismo)
    for algarismo in l:  # Adiciona x na lista nova e o remove da original
        if algarismo == x:
            l_nova.append(algarismo)
            l.remove(algarismo)
            break
    l_nova.extend(l)  # Adiciona o que restou da lista original na lista nova
    for posicao, algarismo in enumerate(l_nova):  # Adiquire a nova posicao j do elemento x
        if algarismo == x:
            posicao_nova = posicao
            break
    L = l_nova
    return posicao_nova


print(particiona(L, I), L)
