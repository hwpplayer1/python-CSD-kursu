a = [1, 2, 3, 4, 5]
b = [10, 20, 30]
c = [5, 15, 15, 20, 25, 30]

def foo(x, y, z):
    return x + y + z

for x in map(foo, a, b, c):
    print(x, end = ' ')

print()
