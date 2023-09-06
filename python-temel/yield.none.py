def bar(n):
    for i in range(n):
        print('New iteration')
        yield i
    print('end')

print(type(bar))            # <class 'function'>

g = bar(3)
print(type(g))              # <class 'generator'>

for i in g:
    print(i)
