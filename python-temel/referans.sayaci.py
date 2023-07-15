def foo(x):
    print(x)                         # RS: 4

a = 10                               # RS: 1
b = a                                # RS: 2
c = b                                # RS: 3
foo(c)                               # RS: 3

c = 'ali'                            # RS: 2
b = 'veli'                           # RS: 1
a = 'selami'                         # RS: 0
