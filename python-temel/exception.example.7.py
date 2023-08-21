def foo(a):
    print('foo başladı...')
    if not isinstance(a, int):
        raise TypeError
    if a < 0:
        raise ValueError
    print('foo ok')

try:
    foo('ali')
except ValueError:
    print('Sayı istenildiği gibi değil!')
except TypeError:
    print('Sayı int türden değil!')

print('son...')
