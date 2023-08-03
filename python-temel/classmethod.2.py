class Sample:
    def __init__(self):                        #örnek metodu
        self.a = 10

    def foo(self):                             #örnek metodu
        print('foo')

    @staticmethod
    def bar():                                 # statik metot
        print('bar')

    @classmethod                               # sınıf metodu
    def tar(cls):
        print('tar')


s = Sample()
s.foo()                                         # örnek foo metodu çağrılır

Sample.bar()                                    # statik bar metodu
Sample.tar()                                    # Sınıf tar metodu, Sample cls pa

s.bar()                                         # statik bar metodu
s.tar()                                         # sınıf tar metodu, Sample cls parametresi olarak geçirilir

