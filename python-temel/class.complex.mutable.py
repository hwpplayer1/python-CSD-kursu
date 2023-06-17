class Complex:
    def set(self, real, imag):
        self.real = real
        self.imag = imag

    def disp(self):
        print("{}+{}i".format(self.real, self.imag))

z1 = Complex()
z2 = Complex()

z1.set(2, 3)
z2.set(4, 5)

z1.disp()
z2.disp()
