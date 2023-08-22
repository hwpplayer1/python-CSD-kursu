def bar(a):
    print('bar begins...')

    try:
        if not isinstance(a, int):
            raise TypeError
        if a < 0:
            raise ValueError
    except ValueError:
        print('İç try deyiminin ValueError except bloğu')

    print('bar ends...')


def foo(a):
    print('foo begins...')
    bar(a)
    print('foo ends...')

try:
    foo(-1)
except TypeError:
    print('Dış try deyiminin TypeError except bloğu')
except ValueError:
    print('Dış try deyiminin ValueError except bloğu')

print('program sonlanıyor...')
