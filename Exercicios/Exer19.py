def separador(e):
    n_sinais, n1, n2, op1 = e.count('+') + e.count('-'), '', '', ''
    if n_sinais != 1:  # Se ha um sinal no primeiro numero, eu adiciono ele ao operador1 e deleto da equacao
        op1 += e[0]
        e = e.replace(e[0], '', 1)
    ec = e[:]
    for x in e:       # adiciono todos os algarismos do primeiro numero em n1
        if x == '+' or x == '-':
            break
        n1 += x
        ec = ec.replace(x, '', 1)  # retiro n1 de ec(copia de e), assim transformando-o em operador2 + n2
    op2 = ec[0]  # Adiquiro o operador2
    n2 = ec[1:]       # Adiquiro o segundo numero
    return n1, n2, op1, op2


class NumeroDecimal:
    def __init__(self, v, op):
        self.op = op
        while v[0] == '0':        # Retiro os 0's a esquerda do numero
            v = v.replace('0', '', 1)
        self.v = v

    def __add__(self, other):
        n1, n2, i1, i2 = self.transf_float_int(other)  # Uso a funcao para alcancar a precisao infinita
        n1, n2 = int(n1), int(n2)
        soma = str(n1 + n2)
        soma = soma[:max(i1, i2)] + ',' + soma[max(i1, i2):]  # Corrijo a formatacao do resultado
        return soma

    def __sub__(self, other):
        n1, n2, i1, i2 = self.transf_float_int(other)  # Uso a funcao para alcancar a precisao infinita
        n1, n2 = int(n1), int(n2)
        sub = str(n1 - n2)
        sub = sub[:max(i1, i2)] + ',' + sub[max(i1, i2):]  # Corrijo a formatacao do resultado
        return sub

    def __repr__(self):
        return self.v.replace('.', ',', 1)

    def transf_float_int(self, other):
        if '.' not in self.v:         # Pego a posicao dos pontos
            i1, i2 = len(self.v) + 1, other.v.index('.') + 2
        elif '.' not in other.v:
            i1, i2 = self.v.index('.') + 2, len(other.v) + 1
        else:
            i1, i2 = self.v.index('.'), other.v.index('.')
        if len(self.v) - i1 == len(other.v) - i2:  # Vejo se os numeros possuem quantidade de casas decimais iguais
            return self.op + self.v, other.v  # Adiciono ao numero1 seu operador e os retorno
        else:
            if len(self.v) > len(other.v):  # Descubro qual deles e maior
                menor, maior = other.v, self.v
            else:
                menor, maior = self.v, other.v
        while len(menor) - i1 < len(maior) - i2:  # Adiciono 0's a direita do float com menos casas decimais
            menor += '0'
        if maior == self.v:             # Adiciono o operador ao numero_1 e mudo os nomes para n1 e n2
            menor, maior = menor, self.op + maior
            n1, n2 = menor, maior
        else:
            menor, maior = self.op + menor, maior
            n1, n2 = maior, menor
        n1, n2 = n1.replace('.', '', 1), n2.replace('.', '', 1)
        print(n1, n2, i1, i2)
        return n1, n2, i1, i2


equacao = input()
num1, num2, operador1, operador2 = separador(equacao)
a = NumeroDecimal(num1, operador1)
b = NumeroDecimal(num2, operador2)
print(a.v, a.op)
print(b.v, b.op)
if operador2 == '+':
    print(a+b)
else:
    print(a-b)

