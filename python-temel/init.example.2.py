class A:
    def __init__(self):
        print('A.__init__')

class B:
    def __init__(self):
        print('B.__init__')

class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')

c = C()
