class Sample:
    def foo(self):
        print("Sample.foo")

class Mample:
    def foo(self):
        print("Mample.foo")

s = Sample()
m = Mample()

s.foo()
m.foo()

Sample.foo(s)
Mample.foo(m)
