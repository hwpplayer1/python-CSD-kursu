class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.__mro__)
