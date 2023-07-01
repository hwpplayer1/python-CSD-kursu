import inspect

class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(inspect.getmro(C))
