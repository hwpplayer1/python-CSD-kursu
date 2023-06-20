class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def disp(self):
        print(self.a, self.b)

x = Sample(10, 20)
x.disp()
