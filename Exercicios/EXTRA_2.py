#A implementacao de arvore binaria a seguir é bem mais simples, com poucos métodos:
#o add adiciona um número na arvore, mantendo as determinacoes de ordem (se for maior vai a esquerda e se for menor vai a direita)
#o find retorna uma lista com o caminho percorrido até aquele determinado numero
#é importante dizer que o print nesse caso imprime uma lista contendo todos os nós da arvore, onde cada nó possui sua própria lista do tipo [nó, esquerda, direita]
class arvbin:

    def __init__(self, first_num=None):
        self.first_num = first_num

    def add(self, num_adicionado):
        if self.first_num == None:
            self.first_num = num_adicionado
        else:
            pointer = self.first_num
            while(True):
                if (num_adicionado.number > pointer.number):
                    if (pointer.posterior == None):
                        pointer.posterior = num_adicionado
                        break
                    else:
                        pointer = pointer.posterior
                else:
                    if (pointer.anterior == None):
                        pointer.anterior = num_adicionado
                        break
                    else:
                        pointer = pointer.anterior

    def find(self,num):
        path = []
        list_item = self.first_num
        while (list_item.number != num):
            path.append(list_item.number)
            if list_item.number < num:
                list_item = list_item.posterior
            else:
                list_item = list_item.anterior
        path.append(list_item.number)
        return path

    def __repr__(self):
        return str([self.first_num.number, self.first_num.anterior, self.first_num.posterior])

class node:
    def __init__(self, number,anterior=None,posterior=None):
        self.number = number
        self.anterior = anterior
        self.posterior = posterior

    def __repr__(self):
        return str([self.number, self.anterior, self.posterior])

a = arvbin()
a.add(node(5))
a.add(node(3))
a.add(node(7))
a.add(node(1))
a.add(node(6))
a.add(node(4))
a.add(node(8))
a.add(node(0))
print(a)
print(a.find(0))