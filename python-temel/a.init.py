class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    pass

print(B.__mro__)            # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
b = B()                     # A.__init__ çağrılır
