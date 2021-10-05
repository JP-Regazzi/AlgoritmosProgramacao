# Mostrar todos os numeros primos de um intervalo [0:n] (incluindo n)
while True:
    lista_primos = [2]
    n_divisores = 0
    n = int(input('Por favor digite um numero inteiro, que sera mostrado todos os numeros primos do intervalo [0,n] '))

    for numero in range(1, n+1, 2):
        for divisor in range(1, numero+1, 2):
            if numero % divisor == 0:
                n_divisores += 1

        if n_divisores == 2:
            lista_primos.append(numero)
            n_divisores = 0
        else:
            n_divisores = 0

    print(f'{lista_primos}' + '\n')
