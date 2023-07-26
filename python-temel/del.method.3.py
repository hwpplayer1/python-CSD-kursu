class A:
    def __init__(self):
        super().__init__()
        print('A.__init__ called')

    def __del__(self):
        print('A.__del__ called')
        super().__del__()

class B:
    def __init__(self):
        super().__init__()
        print('B.__init__ called')

    def __del__(self):
        print('B.__del__ called')

class C(A):
    def __init__(self):
        super().__init__()
        print('C.__init__ called')

    def __del__(self):
        print('C.__del__ called')
        super().__del__()

class D(B):
    def __init__(self):
        super().__init__()
        print('D.__init__ called')

    def __del__(self):
        print('D.__del__ called')
        super().__del__()

class E(C, D):
    def __init__(self):
        super().__init__()
        print('E.__init__ called')

    def __del__(self):
        print('E.__del__ called')
        super().__del__()

e = E()
e = None
print(E.__mro__)
