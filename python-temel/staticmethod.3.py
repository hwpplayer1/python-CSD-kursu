class Sample:
    def foo(self):
        print('foo')

    @staticmethod
    def bar(self):
        print('bar')

s = Sample()
s.foo()                      # Sample.foo(s)
s.bar(10)                    # geçerli, 10 burada self'e atanacak
#s.bar()                      # exception, çünkü self sıradan bir parametre