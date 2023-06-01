a = [1, 2, 3, 4, 5]

def foo(n):
    return n * n

b = map(foo, a)
print(list(b))
