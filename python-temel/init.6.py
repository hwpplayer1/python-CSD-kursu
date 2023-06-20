class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def disp(self):
        print('{}+{}i'.format(self.real, self.imag))

z1 = Complex()
z1.disp()

z2 = Complex(10)
z2.disp()

z3 = Complex(10, 20)
z3.disp()
