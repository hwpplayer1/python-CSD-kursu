class Sample:
    def foo():
        print('static foo method')

    foo = staticmethod(foo)


Sample.foo()
