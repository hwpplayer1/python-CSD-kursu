class Sample:
    def __init__(self, a):
        self._a = a

    def disp(self):
        print(self._a)

    def __foo(self):
        print('Sample.__foo')


s = Sample(10)
s.disp()
s._a = 20                 # kötü teknik, _ ile başlatılan değişkenler dışarıdan kullanılmamalıdır
s._Sample__foo()          #
#s.__foo()                # exception!
