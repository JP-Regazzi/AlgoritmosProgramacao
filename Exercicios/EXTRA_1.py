# Lista encadeada em classe

class ListaEncadeada:
    def __init__(self, node=None):
        self.node = node

    def empty(self):
        return self.node == None

    def add(self, x):
        if self.empty():
            self.node = noh(x)
        else:
            # self.node = noh(x, self.node)
            self.node = noh(x, ListaEncadeada(self.node))
    def remove(self):
        self.node = self.next().node

    def value(self):
        return self.node.valor

    def next(self):
        return self.node.next

    def __repr__(self):
        l = self
        s = '['
        while not l.empty():
            s += str(l.value()) + ','
            l = l.next()
            if l == None: break
        s += '\b]'
        return s

class noh:
    def __init__(self, valor, next=None):
        self.valor, self.next = valor, next

x = ListaEncadeada()
x.add(100)
x.add('luidi')
x.add(-1)
x.add([0,1])
x.add('parede')

print(x)
print(x.next())
x.next().remove()

print(x)
print(x.next())

