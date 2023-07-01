class A:
    def __init__(self, a):
        self.a = a

    def dispA(self):
        print(self.a)

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b

    def dispB(self):
        print(self.b)

b = B(10, 20)
b.dispA()
b.dispB()
