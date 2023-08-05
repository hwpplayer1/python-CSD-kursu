class foo:
    def __init__(self, f):
        print('ilk işlemler')
        self.f = f

    def __call__(self):
        print('araya giren işlemler')
        self.f()

@foo
def bar():
    print('bar')

bar()               # aslında bar.__call__() çağrısı yapılıyor
