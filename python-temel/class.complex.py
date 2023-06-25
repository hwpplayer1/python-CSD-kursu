class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def disp(self):
        print('{}+{}i'.format(self.real, self.imag))

    def add(self, z):
        result = Complex()
        result.real = self.real + z.real
        result.imag = self.imag + z.imag

        return result

z1 = Complex(10, 20)
z2 = Complex(3, 4)
z3 = z1.add(z2)

z1.disp()
z2.disp()
z3.disp()
