'''Metodos de lista
numeros = [5, 2, 1, 5,  7, 4]
numeros2 = numeros.copy()
print(numeros2)
numeros.append(20)
numeros.pop()
numeros.insert(0, 10)
numeros.remove(2)
print(numeros.index(7))
print(5 in numeros)
print(numeros.count(5))
print(numeros)
numeros.sort()
numeros.reverse()
print(numeros)
numeros.clear()
print(numeros)

Exercicio: tirar caracteres repetidos de uma lista

lista = eval(input('digite uma lista '))
print(f'Lista original: {lista}')
for caracter in lista:
    while lista.count(caracter) > 1:
        lista.remove(caracter)
print(f'Lista sem itens repetidos: {lista}')

# Tuples (tipo listas mas n podemos modifica-las)
numeros = (1, 2, 3)
print(numeros[0])

# Desempacotamento
coordenadas = (1, 2, 3)
xingamentos =['arrombado', 'viado', ' escroto', 'viado', 'esculhanbado', 'escroto', 'pra', 'caralho']
x, y, z = coordenadas
a, b, c, d, e,f, g, h = xingamentos
print(z)
print(c)

# Dicionarios (pode ser qualquer coisa o valor - lista, string, numero, valor booleano...)
usuario = {
    'nome': 'Joao Pedro',
    'idade': 30,
    'verificadinho': True
}
usuario['nome'] = 'Carlos Alberto'
usuario['cor_do_cabelo'] = 'Loiro'
print(usuario['nome'])
print(usuario.get('cu', 'comi sua mae'))
print(usuario.get('idade'))

# Exercicio: pessoa digita algarismos e vc devolve os numeros em portugues

numero_portugues = {
    '9': 'nove ',
    '8': 'oitro',
    '7': 'sete',
    '6': 'seis',
    '5': 'cinco',
    '4': 'quatro',
    '3': 'treis',
    '2': 'dois',
    '1': 'um',
    '0': 'zero'
}
celular = input('Por favor, digite seu numero de celular a seguir: ')
str_saida = ''
for numero in celular:
    str_saida += numero_portugues.get(numero, 'digite um numero') + ' '
print(str_saida)

# Conversor de EMOJIS

mensagem = input('> ')
palavras = mensagem.split(' ')
emojis = {
    ':)': '😀',
    ':(': '😢'
}
saida = ''
for palavra in palavras:
    saida += emojis.get(palavra, palavra) + ' '
print(saida)

# Funcoes

def saudacoes():
    print('Ola')
    print('Bem vindo')


print('Comecar')
saudacoes()
print('FIM')

# Parametros      OBS: PARAMETRO BURACO ONDE COLOCA INFORMACAO; ARGUMENTO E A INFORMACAO QUE SE COLOCA


def xingamentos(nome, casa):
    print('Se fuder seu arrombado de merda eu espero que vc morra se cuzao ')
    if casa == 'zona sul':
        print('riquinho de merda eu sei onde vc mora e sei seu nome', nome, 'vai morrer estrume')
    else:
        print('pobretao de merda n consegue melhorar na vida dependente quimico morador de favela', nome, 'vai morrer')
    return 'quem leu e gay'


xingamentos(input('Qual o seu nome amigo?'), input('Onde vc mora irmao?'))

# Arggumentos de palavra-chave (no de cima usei argumentos de posicao) obs-> argumento palavra-chave tem q vir dps

print(xingamentos(casa=input('Tudo bem chapinha?, me digite onde vc mora '), nome=input('Tem nome gostoso? ')))

# Comando de return (geralmente uso pra calculacoes)


def media_geometrica(lista_valores):
    media = 1
    quantidade = len(lista_valores)
    for xi in lista_valores:
        media *= xi
    return media ** 1/quantidade


def media_aritimetica(lista_valores):
    for xi in lista_valores:
        media += xi/len(lista_valores)
    return med_arit


print(media_geometrica(eval(input('vai'))))

# Recursao


def fun(k, n=0, arr=[]):
    "retorna uma lista com todos os numeros de n ate k"
    if n == k:
        return
    else:
        arr.append(n)
        fun(k, n+1, arr)
    return arr'''


def listFlatten(inputList):
    for i in inputList:
        if type(i) == int:
            outputList.append(i)
        elif type(i) == list:
            listFlatten(i)
    return outputList

