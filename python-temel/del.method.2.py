class A:
    def __init__(self):
        print('A.__init__ called')

    def __del__(self):
        print('A.__del__ called')

class B(A):
    def __init__(self):
        super().__init__()
        print('B.__init__ called')

    def __del__(self):
        print('B.__del__ called')
        super().__del__()

b = B()
b = None
        
