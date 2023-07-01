class A:
    def setA(self, a):
        self.a = a

    def dispA(self):
        print(self.a)

class B(A):
    def setB(self, b):
        self.b = b

    def dispB(self):
        print(self.a, self.b)

b = B()

b.setA(10)
b.setB(20)

b.dispA()
b.dispB()
