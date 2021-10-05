# Questao 3 da prova


X, N = float(input()), int(input())
def serie_leibniz(x, n):
    soma = 0
    for i, a in enumerate(range(1, n*2, 2)):
        print(a)
        soma += ((-1)**i)*(x**a)/a
    return soma


print(serie_leibniz(X, N))
