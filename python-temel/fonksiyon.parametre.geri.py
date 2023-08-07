def bar(a, b, c):
    print(f'bar çağrıldı: {a}, {b}, {c}')
    def tar(f):
        print(f'tar çağrıldı: {a}, {b}, {c}')
        def zar():
            print(f'Araya girecek kod: {a}, {b}, {c}')
            f()
            return f
        return zar
    return tar
@bar('ali', 'veli', 'selami')
def foo():
    print('foo çağrıldı')

# foo = bar('ali', 'veli', 'selami')(foo)

foo()
foo()
foo()
