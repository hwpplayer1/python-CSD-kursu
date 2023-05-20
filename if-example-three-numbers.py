a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
