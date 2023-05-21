a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

max = a if a > c else c if a > b else b if b > c else c
print(max)
