class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, D):
    pass

print(E.__mro__)    #  (<class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.D'>, <class '__main__.C'>, <class 'object'>)


    
