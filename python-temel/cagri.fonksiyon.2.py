def foo(a, b, c, d, e):
    print(a, b, c, d, e)

def bar(*a):
    foo(*a)

l = [10, 20, 30, 40, 50]
bar(*l)