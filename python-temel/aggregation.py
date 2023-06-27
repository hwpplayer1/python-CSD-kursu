class A:
    pass

class B:
    def __init__(self, a = None):
        self.a = a
        pass

    def seta(self, a):
        self.a = a

a = A()
#print(a)
b1 = B()
#print(b1)
