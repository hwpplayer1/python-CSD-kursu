class Sample:
    def __init__(self, x):
        self.x = x
        print('Sample.__init__ called: {}'.format(x))

    def __del__(self):
        print('Sample.__del__ called: {}'.format(self.x))

a = Sample(10)
b = Sample(20)

def foo():
    x = Sample(30)
    y = Sample(40)

print('first')
foo()
print('second')
