def foo():
    print('foo begins...')
    bar()
    print('foo ends...')

def bar():
    print('bar begins...')
    int('xxx')     # ValueError
    print('bar ends...')

try:
    foo()
except ValueError:
    print("ValueError exception'ı oluştu")
except TypeError:
    print("TypeError exception'ı oluştu")
except IndexError:
    print("IndexErrorexception'ı oluştu")
print('ends...')

    
