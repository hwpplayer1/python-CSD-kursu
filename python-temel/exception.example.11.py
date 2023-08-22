def bar(a):
    print('bar begins...')

    if not isinstance(a, int):
        raise TypeError('Değer int türden değil!')
    if a < 0:
        raise ValueError('Değer negatif!')
    print('bar ends...')

def foo(a):
    print('foo begins...')
    bar(a)
    print('foo ends...')

try:
    foo(-10)
except TypeError as e:
    print('Exception:', e.args[0])
except ValueError as e:
    print('Exception:', e.args[0])
finally:
    print('finally!..')

print('ends..')
