def foo():
    print("bir")
def bar():
    print("iki")
def tar():
    print("üç")
def car():
    print("dört")
def zar():
    print("beş")

d = {1: foo, 2: bar, 3: tar, 4: car, 5: tar}

n = int(input("Bir değer giriniz:"))

if n >= 1 and n <= 5:
    d[n]()
else:
    print("hiçbiri")
