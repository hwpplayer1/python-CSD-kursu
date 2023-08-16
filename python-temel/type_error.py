def foo():
    return 10 + 'ali'

try:
    print('enters the try statement...')
    foo()
except TypeError:
    print('ValueError occurs...')
print('continues...')
