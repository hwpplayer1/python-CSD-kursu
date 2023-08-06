class Mample:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        print('Her Sample nesnesi yaratıldığında araya giren kod')
        return self.cls(*args, **kwargs)

def foo(cls):
    return Mample(cls)

@foo
class Sample:
    def __init__(self, a):
        self.a = a

    def bar(self):
        print('bar')

s = Sample(10)
s.bar()
