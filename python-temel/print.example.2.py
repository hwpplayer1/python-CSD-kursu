class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return '{}+{}i'.format(self.real, self.imag)

z = Complex(3, 2)
print(z)
