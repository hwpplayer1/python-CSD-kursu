def foo():
    print('foo begins...')
    try:
        bar()
    except ValueError:
        print('yanlış değer')
    print('foo ends...')


def bar():
    print('bar begins...')
    tar()
    print('bar ends...')

def tar():
    print('tar begins...')
    val = int(input('Bir değer giriniz:'))
    print('tar ends...')

foo()
