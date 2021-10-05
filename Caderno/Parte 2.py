# import random
'''# Operadores Logicos
has_good_credit = True
has_high_income = False
has_criminal_record = True
if has_good_credit and has_high_income:
    print('Aceitavel para varios emprestimos')
elif has_good_credit and not has_criminal_record:
    print('Pode pegar algumns creditos')
else:
    print('Voce e um merda, vaza')


# Operadores de Comparacao
temperatura = int(input('Qual a temperatura em Celsius?'))
if temperatura > 30:
    print('Hoje e um dia quente')
elif temperatura < 18:
    print('Hoje e um dia frio')
else:
    print('Hoje a temperatura esta agradavel')
nome = input('Qual seu nome?')
nome2 = 'a'
if len(nome) > 50:
    print('Insira um nome com menos de 50 caracteres por favor')
    nome2 = input('Qual seu nome?')
elif len(nome) < 3:
    print('Insira um nome com mais de 3 caracteres por favor')
    nome2 = input('Qual seu nome?')
else:
    print('Obrigado pela informacao!!')

if 3 < len(nome2) < 50:
    print('Obrigado pela informacao')


# Programa Conversor de Peso
peso = float(input('Digite seu peso '))
medida = input('Digite L ou K para determinar qual a medida do peso informado ').upper()
if medida == 'L':
    print(f'Seu peso em quilos equivale a {round(peso / 2.2, 2)}')
elif medida == 'K':
    print(f'Seu peso em libras equivale a {round(peso * 2.2, 2)}')
else:
    input('Por favor renicie o programa e indique seu peso novamente')


# While Loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('done')


# Jogo de Adivinhar - infinito e resposta variando (import random)
resposta = random.randint(1, 10)
t1 = int(input('Adivinhe um número de 1 a 10 '))
while t1 != resposta:
    print(f'A resposta era {resposta}')
    t1 = int(input('Adivinhe um número de 1 a 10 novamente '))
    resposta = random.randint(1, 10)
print('Parabéns você acertou!!!')


# Jogo de Adivinhar - l_tentativas e resposta constante
numero_secreto = random.randint(1, 10)
numero_tentativas = 1
limite_tentativas = 5
tentativa = 0
while numero_tentativas <= limite_tentativas:
    tentativa = int(input(f'Adivinhe um número de 1 a 10, esta é sua {numero_tentativas}ª tentativa!'))
    numero_tentativas += 1
    if tentativa == numero_secreto:
        print('Parabéns você acertou!!!')
        break
    elif tentativa != numero_secreto:
        print(f'Sua {tentativa}ª tentativa estava errada.')
else:
    print('Você perdeu! Que pena, mas ainda pode tentar novamente! :)')


# For loop
for item in [173, -10]:
    print(item)
for maia in range(0, 10, 2):
    print(maia)
# Calculadora do preço
sacola = [10, 9, 15, 4]
total = 0
for precos in sacola:
    total += precos
print(f'O preço total da compra é de ${total}')


# Nested loops - loop dentro de outro
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# Desafio
numbers = [5, 2, 5, 2, 2]
letra = 'x'
for x_count in numbers:
    print(f'{x_count * letra}')

# ou
numeros = [2, 2, 2, 2, 6]
for quantidade_de_x in numeros:
    saida = ''
    for quantidade in range(quantidade_de_x):
        saida += 'x'
    print(saida)

# Listas
xingamentos = ['Cu', 'Caralho', 'Arrombado', 'Fudido', 'Cuzao']
print(xingamentos[2:4])
print(xingamentos[:-1])
print(xingamentos[:])
xingamentos[0] = 'CORNO'
print(xingamentos)


# Desafio de lista - achar o maior numero na lista
lista = [2, 3, 5, 8, 9, 54, 12, 7, 9]
maximo = lista[0]
for numero in lista:
    if numero > maximo:
        maximo = numero
print(maximo)
# OBS "For item in lista" pode ser pensado como uma funcao que transforma o item no que esta na lista a quantidade
# de vezes que quisermos. Cada metamorfose ocorre quando quando a "primeira leva" do codigo terminar.'''


Listas 2D

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
matrix[2][2] = 20
print(matrix[2][2])

maximo = 0
for linha in matrix:
    for item in linha:
        if maximo < item:
            maximo = item
        print(item)
print(maximo)





