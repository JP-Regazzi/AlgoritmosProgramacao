# import time
# Video Programacao orientada a objetos
'''x = 1
y = 'eae' '''
# OBS: y+x seria um erro (objetos de tipos diferentes)

# Metodos podem ser performados em objetos:
'''print(y.upper()) '''
# OBS: x.upper daria erro (esse metodo nao funciona para tipo int)

# CRIAR A PROPRIA CLASSE:

'''
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pegar_nome(self):
        return self.nome

    def pegar_idade(self):
        return self.idade

    def mudar_idade(self, idade):
        self.idade = idade

    def miau(self, n):
        return f'{n} miados'

    def latir(self):
        print('woof')


c = Cachorro('Toto', 12)
print(type(c))
c.latir()
print(c.miau(3))
print(c.nome)
c2 = Cachorro('Jorge', 4)
print(c2.pegar_nome())
print(c.pegar_idade())
c2.mudar_idade(20)
print(c2.pegar_idade())
'''

# Exemplo mais avancado:
'''

class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota  # 0 - 100

    def pegar_nota(self):
        return self.nota


class Curso:
    def __init__(self, nome, vagas):
        self.nome = nome
        self.vagas = vagas
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        if len(self.estudantes) < self.vagas:
            self.estudantes.append(estudante)
            return True
        return False

    def pegar_nota_media(self):
        valor = 0
        for estudante in self.estudantes:
            valor += estudante.pegar_nota()
        return valor/len(self.estudantes)


e1 = Estudantes('Nicholas', 19, 95)
e2 = Estudantes('Barros', 18, 80)
e3 = Estudantes('Ygor', 18, 30)

curso = Curso('Computaria', 2)
curso.adicionar_estudante(e1)
curso.adicionar_estudante(e2)
print(curso.estudantes[0].nome)
print(curso.pegar_nota_media())
print(curso.adicionar_estudante(e3))'''

# Conceito um pouco mais complexo - Duas classes muito parecidos (INERENTES)
'''
class Gato:
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print('Miau!')


class Cachorro:
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print('Woof!') '''  # Desse modo escrevemos mais do que o necessario

# Usando a classe pet podemos ser mais produtivos- PET e uma classe geral

'''
class Pet:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f'EU sou {self.nome} e tenho {self.idade} anos')

    def falar(self):
        print('Nao sei oq falar')


class Gato(Pet):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)  # super = classe que essa esta inerente
        self.cor = cor

    def falar(self):
        print('Miau!')

    def mostrar(self):
        print(f'EU sou {self.nome}, tenho {self.idade} anos e sou {self.cor}')


class Cachorro(Pet):
    def falar(self):
        print('Woof!')


class Raposa(Pet):
    pass


p = Pet('Thomas', 4)
p.mostrar()
p.falar()
g = Gato('Penny', 6, 'cinza')
g.mostrar()
g.falar()
c = Cachorro('Toto', 12)
c.mostrar()
c.falar()
r = Raposa('Ladroa', 14)
r.mostrar()
r.falar()'''

# Exemplo extra de heranca, fiz de PRATICA

'''
class Veiculo():
    def __init__(self, preco, gasolina, cor):
        self.preco = preco
        self.gasolina = gasolina
        self.cor = cor

    def encher_tanque(self):
        self.gasolina = 100

    def esvaziar_tanque(self):
        self.gasolina = 0

    @staticmethod
    def gasolina_atual(self):
        return self.gasolina

class Carro(Veiculo):
    def __init__(self, preco, gasolina, cor, velocidade):
        super().__init__(preco, gasolina, cor)
        self.velocidade = velocidade

    @staticmethod
    def buzina(self):
        print('BI BI!!')

class Caminhao(Veiculo):
    def __init__(self, preco, gasolina, cor, carga):
        super().__init__(preco, gasolina, cor)
        self.carga = carga

    @staticmethod
    def quanta_carga(self):
        return self.carga

    @staticmethod
    def buzina(self):
        print('FON FON!')


picudo = Caminhao(100000, 70, 'amarelo', 300)
mercedes = Carro(1000000, 50, 'azul', 280)
Caminhao.buzina(picudo)
Carro.buzina(mercedes)
print(Caminhao.quanta_carga(picudo))
print(Veiculo.gasolina_atual(picudo))
print(Veiculo.gasolina_atual(mercedes))
Veiculo.esvaziar_tanque(picudo)
Veiculo.esvaziar_tanque(mercedes)
print(Veiculo.gasolina_atual(picudo))
print(Veiculo.gasolina_atual(mercedes))'''

# Atributos de classe

'''
class Pessoa:
    numero_de_pessoas = 0  # Atributo (algo p se atribuir para toda a classe, tipo gravidade em humanos do rj)
    nomes_das_pessoas = []

    def __init__(self, nome):
        self.nome = nome
        Pessoa.numero_de_pessoas += 1
        Pessoa.nomes_das_pessoas.append(nome)

print(Pessoa.nomes_das_pessoas)
p1 = Pessoa('Timmy')
print(Pessoa.numero_de_pessoas)
p2 = Pessoa('Carlos')
print(Pessoa.numero_de_pessoas)
Pessoa.numero_de_pessoas = 8
print(p2.numero_de_pessoas)
print(p1.nomes_das_pessoas)  # PODE CHAMAR COM O NOME DA CLASSE OU COM UM OBJETO DA CLASSE'''

# Metodos de classe - pode ser chamada em qualquer instancia da classe ou com nome da classe
'''

class Pessoa:
    numero_de_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.adicionar_pessoa()

    @classmethod
    def numero_de_pessoas_f(cls):  # Precisa no minimo do parametro cls, mas pode ter outros tambem
        return cls.numero_de_pessoas

    @classmethod
    def adicionar_pessoa(cls):
        cls.numero_de_pessoas += 1


p1 = Pessoa('Timmy')
p2 = Pessoa('Carlos')
print(Pessoa.numero_de_pessoas_f())  # Podemos colocar um objeto dentro dos parenteses mas n precisa'''

# Metodos estaticos - podemos criar classes para organizar funcoes (tipo o modulo math)
                        # Eles so tem acesso a seus proprios parametros. (Ex: n tem acesso a atributos de classe)
'''
class Matematica:  # nem precisa do __init__

    @staticmethod  # fazem algo, mas nao mudam nada (n altera x)
    def adicionar_5(x):
        return x + 5

    @staticmethod  # ele nao precisa do parametro classe para ser chamado (cls) e pode passar qualquer parametro
    def pr():
        print('corra')


print(Matematica.adicionar_5(10))   
Matematica.pr()'''

# Metodos de sobrecarregar/Metodos magicos - Overloading Methods
'''
class Ponto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coordenadas = (self.x, self.y)

    def mover(self, x, y):
        self.x += x
        self.y += y
        self.coordenadas = (self.x, self.y)

    def __add__(self, p):
        return Ponto(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Ponto(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y + p.y

    def distancia(self): ## PODERIA TER USADO O LEN
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.distancia() > p.distancia()

    def __ge__(self, p):
        return self.distancia() >= p.distancia()

    def __lt__(self, p):
        return self.distancia() < p.distancia()

    def __le__(self, p):
        return self.distancia() <= p.distancia()

    def __eq__(self, p):
        return round(self.distancia()) == round(p.distancia())

    def __str__(self):
        return f'{self.coordenadas}'

px = Ponto(5, 0)
p1 = Ponto(3, 4)
p2 = Ponto(3, 2)
p3 = Ponto(1, 3)
p4 = Ponto(0, 4)
p5 = p1 + p2
p6 = p1*p2
p7 = p1-p4
print(p5)
print(p6)
print(p7)
print(p1 > p4)
print(p1 == px)
p2.mover(1,1)
print(p2)'''

# Classes publicas e privadas
'''
class _Privada:  # O underline e para mostrar para o programador que essa classe/ funcao e privada
    def __init__(self, nome):
        self.nome = nome


class NaoPrivada:
    def __init__(self, nome):
        self.nome = nome
        self.priv = _Privada(nome)

    def _display(self):  # Classes/ Funcoes privadas nao deveriam ser chamadas em outros arquivos
        print('Ola!')

    def display(self):
        print('Oi!')'''


################ EXTRAS ################


# Funcao Mapa ( Map function) - permite a facil aplicacao de uma funcao em uma lista
'''
l = [1,2,3,4,5,6,7,8,9,10]

def func(x): # Quero aplicar essa funcao na lista e, entao, salvar essa nova lista  (poderia ser feito com for)
    return x**x

print(list(map(func, l)))  # Funcao map recebe uma funcao e uma lista, e retorna a lista apos aplicacao da funcao
print([func(x) for x in l]) # Equivalente a usar a funcao map
print([func(x) for x in l if x%2==0])  # so legalzinho (so usa e utilizado os numeros pares da lista)
'''


# Funcao Filtro (Filter function) - A funcao filter recebe uma lista e uma funcao, como a map function
'''
def adicionar7(x):
    return x+7

def impar(x):
    return x%2 != 0  # OBS: Python considera tudo que nao seja 0, vazio ou False como True

def par(x):
    return x%2 == 0
a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(impar, a)) # Se a funcao retornar True, o valor e adicionado a lista return, caso contrario, nao
c = list(filter(par, a))
print(b, c)


# Funcao Lambda (Funcao Anonima) - serve p funcoes que cabem em so uma linha

def func(x):
    func2 = lambda x: x + 5  # Com elas podemos criar rapidamente uma funcao pequena
    return func2(x) + 100

func3 = lambda x, y=1: x + y  # Lembrete, se eu n colocar nada no local do y, ele vai como 1 de padrao(PARAMETRO OPCIONAL)
                              # Pode se usar multiplos parametros opcionais, o valor default geralemte e o mais comum

print(func(2), func(1), func3(1,10))

# Exemplo de Lambda

a = [1,2,3,4,5,6,7,8,9,10]
nova_lista = list(map(lambda x: x+5, a))
lista_pares = list(filter(lambda x: x%2==0, a))
print(nova_lista, lista_pares)

lista_usando_tudo = list(map(lambda x: x+10, filter(impar, a)))  # a funcao impar ta la em cima
print(lista_usando_tudo)'''

##### ERROS E EXCECOES  - OBS: SE EXCEP ATIVAR, O CODIGO NAO PARA, ELE SO NAO FAZ OQ ESTA LIGADO AO TRY

# Try
'''
x = 1
y = float(input())
l = [1,2,3,4]
try:
    z = x/y
    print(z)
    print(l[int(z)])
except ZeroDivisionError:
    print('Nao e possivel dividir por 0')
except IndexError:
    print('Nao foi possivel alcancar o indice buscado')

# Classe mais alta deve sempre vir depois da classe mais baixa  (classe mais baixa esta contida na mais alta)

try:
    z = x/y
except ArithmeticError:
    print('Erro de aritmetica')
    z = 1 / 0
except ZeroDivisionError:
    print('Erro de divisao por 0')

# Else

try:
    z = x/y
except ZeroDivisionError:
    print('Terceiro erro de zero cacilda')
else:
    print('foi')

# Finaly    - Finaly sempre sera executado imediatamente antes da instrucao break, continue ou return

def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return())

# OBS: Finaly tbm e executado se houver um erro nao tratado


# Clase except

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:  # O except que roda primeiro faz com que os de baixo nao sejam lidos
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

for cls in [B, C, D]:  # Como todas as cls rodam o except B, e ele e o primeiro, ele e impresso em todos os casos
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")

# Definindo excecoes

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, expressao, mensagem):
        self.expressao = expressao
        self.mensagem = mensagem

# Raise - Forca a ocorrencia de determinado tipo de excecao - raise classe(mensagem)

try:
    raise NameError('Teste')
except NameError:
    print('Eae')
    raise'''



# Aula do Tech With Tim  de classes





