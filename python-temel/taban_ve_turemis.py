class A:
    def __init__(self):
        print('A __init__ called: {}'.format(type(self)))
        self.x = 10

    def dispA(self):
        print('A.Disp: {}'.format(self.x))

class B(A):
    def __init__(self):
        print('B __init__ called: {}'.format(type(self)))
        super(B, self).__init__()
        self.x = 20

    def dispB(self):
        print('B.Disp: {}'.format(self.x))

b = B()
b.dispB()
b.dispA()
