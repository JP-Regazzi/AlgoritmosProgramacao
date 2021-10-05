'''import math

# Variaveis
full_name = 'John Smith'
age = 20
new_patient = True
# Input
nome = input('What is your name? ')
cor_favorita = input('Qual sua cor favorita? ')
print('Oi ' + nome + ' vejo que voce gosta de ' + cor_favorita)
# Conversa digital
ano_nascimento = input('Ano de nascença: ')
print(type(ano_nascimento))
idade = 2020 - int(ano_nascimento)
print(type(idade))
print(idade)

peso_cliente = input('Qual seu peso em quilos? ')
peso_libras = 2.2046 * float(peso_cliente)
str(peso_libras)
input(peso_libras)'''
# Strings
# curso = '''           "Tutorial" de Python para iniciantes
#  Hoje irei ensina-los o basico do python como por exemplo:
#     -Variaveis
#     -Listas
#     -Cus
#     -Penis
#     ect'''
# print(curso)
# alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# print(alfabeto[0])
# print(alfabeto[20:])
# outra_variavel = alfabeto[:]
# print(outra_variavel)
#
# nome = 'Paulo'
# print(nome[1:-1])

# Formatted Strings
'''primeiro = 'João'
ultimo = 'Silva'
mensagem = primeiro + ' [' + ultimo + '] daltoba'
msg = f'{primeiro} [{ultimo}] daltoba'
print(mensagem)
print(msg)
# String Methods
curso = 'Python para iniciantes'
print(len(curso))
print(curso.upper())
print(curso.lower())
print(curso.find('P'))
print(curso.find('iniciantes'))
print(curso.replace('iniciantes', 'profissionais'))
print('python' in  curso)
# Operações Aritméticas
print(10 + 3)
print(10 - 3)
print(10 * 3 )
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x + 3
x += 3
print(x)
# Ordem das Operacoes
x = 10 + 2 * 3 / (-1//2)
print(x)
# Funcoes Matematicas (import math)- aprender math.
x = 2.9
print(math.ceil(x))
print(math.floor(x))
x = -5.5
print(round(x))
print(abs(x))
# If Statements
is_hot = True
is_cold = False
if is_hot:
    print('É um dia quente')
    print('Beba muita água')
elif is_cold:
    print('É um dia frio')
    print('Use roupas quentes')
else:
    print('É um dia amável')
print('Tenha um bom dia')

preco_da_casa = 1000000
resposta = input('Voce possui bom credito?')
if resposta == 'Sim':
    bom_credito = True
else:
    bom_credito = False
if bom_credito:
    print(f'Voce deve pagar ${int(preco_da_casa * 0.1) } de entrada')
else:
    print(f'Voce deve pagar ${int(preco_da_casa * 0.2) } de entrada')'''

