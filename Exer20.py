class Polinomio:
        # Representa um polinomio de uma variavel

    def __init__(self, coeficientes=[]):
        for x in coeficientes[-1::-1]:
            if x == 0:
                coeficientes.pop(-1)
            else:
                break
        self.coeficientes = coeficientes

    def __setitem__(self, grau, coeficiente):
        while grau+1 > len(self.coeficientes):
            self.coeficientes.append(0)
        self.coeficientes[grau] = coeficiente  # Altera o coeficiente para o termo do grau dado

    def __getitem__(self, grau):
        return self.coeficientes[grau]  # Retorna o coeficiente para o grau dado

    def grau(self):
        return len(self.coeficientes)  # Retorna o grau do polinomio

    def __mul__(self, p):
        resultado, pc, qc = [], self.coeficientes.copy(), p.coeficientes.copy()  # Crio uma copia de q e de p
        resultado += [0 for x in range(len(qc) + len(pc))]  # Determino o numero de casas do resultado
        if len(pc) < len(qc):                   # Faco as duas copias terem o mesmo numero de casas
            for x in range(len(qc) - len(pc)):
                pc.append(0)
        if len(qc) < len(pc):
            for x in range(len(pc) - len(qc)):
                qc.append(0)
        for i1, x in enumerate(qc):
            for i2, y in enumerate(pc):                  # Multiplico qc por pc
                resultado_parcial, indice_parcial = x*y, i1+i2
                resultado[indice_parcial] += resultado_parcial
        multiplicacao = Polinomio(resultado)
        return multiplicacao  # Retorna o polinomio dado pela multiplicacao deste polinomio por p (tambem um polinomio)

    def __add__(self, p):
        resultado, pc, qc = [], self.coeficientes.copy(), p.coeficientes.copy()
        if len(pc) < len(qc):
            for x in range(len(qc) - len(pc)):
                pc.append(0)
        if len(qc) < len(pc):
            for x in range(len(pc) - len(qc)):
                qc.append(0)
        resultado += [x+y for x, y in zip(pc, qc)]
        soma = Polinomio(resultado)
        return soma
        # Retorna o polinomio dado pela soma deste polinomio com p (tambem um polinomio)"

    def __sub__(self, p):
        resultado, pc, qc = [], self.coeficientes.copy(), p.coeficientes.copy()
        if len(pc) < len(qc):
            for x in range(len(qc) - len(pc)):
                pc.append(0)
        if len(qc) < len(pc):
            for x in range(len(pc) - len(qc)):
                qc.append(0)
        resultado += [x - y for x, y in zip(pc, qc)]
        subtracao = Polinomio(resultado)
        return subtracao
        # Retorna o polinomio dado pela diferenca entre este polinomio e p (tambem um polinomio)

    def avalia(self, x):
        valor = 0
        for i, a in enumerate(self.coeficientes):
            valor += a*(x**i)
        return valor  # Retorna a avaliacao do polinomio avaliado em x

    def __repr__(self):
        return f'{self.coeficientes}'


p = Polinomio(eval(input()))
q = Polinomio(eval(input()))
x = input()
if '.' in x:
    x = float(x)
else:
    x = int(x)
print(p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x))

