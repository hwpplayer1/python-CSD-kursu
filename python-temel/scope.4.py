x = 100

def foo():
    x = 200
    print(x)               # yerel 200 çıkar

foo()
print(x)                   # global 100 çıkar
