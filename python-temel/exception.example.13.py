def bar(a):
    print('bar begins...')

    try:
        if not isinstance(a, int):
            raise TypeError
        if a < 0:
            raise ValueError
    except ValueError:
        print('Sayı istenildiği gibi değil')
    finally:
        print('İç try bloğunun finally bölümü')

    print('bar ends...')

def foo(a):
    print('foo begins...')
    bar(a)
    print('foo ends...')

try:
    foo(10.5)
except TypeError:
    print('Sayı int türden değil!')

print('ends..')
