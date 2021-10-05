l = [1,'a',1]

class C:
    a = 1

    def __init__(self,x=[]):

        self.x = x

        C.a = C.a & 1

    def g(self,a):

        self.x += [a]

        self.a += 1

        return C(self.x)

    def __repr__(self):

        return (str(self.x*self.a))

obj = C().g(l[:1])

b = obj.g(l[1:])

print(obj,b)




[(5,6),(1,5),(2,2),(3,4),(0,4),(1,3)]



