class Sample:
    def __init__(self, a):
        self.a = a

    def __call__(self, *args, **kwargs):
        print('a = {}'.format(self.a))
        print('args = {}'.format(args))
        print('kwargs = {}'.format(kwargs))

s = Sample(100)
s(10, 20, 30, xx=40, yy=50)   # eşdeğeri -> s.__call__(10, 20, 30, xx=40, yy=50)
