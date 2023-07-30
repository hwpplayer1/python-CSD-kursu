import math

class Rational:
    def __init__(self, a=0, b=1):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('numerator and denominator must be int!')

        if b == 0:
            raise ValueError('denominator must not be 0!')
        self.a = a
        self.b = b

        self._simplify()


    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        if self.a == 0:
            return '0'

        return f'{self.a}/{self.b}'

    def _simplify(self):
        gcd = math.gcd(self.a, self.b)

        self.a //= gcd
        self.b //= gcd

    def __add__(self, r):
        if isinstance(r, int):
            a = r * self.b + self.a
            b = self.b
        else:
            a = self.a * r.b + self.b * r.a
            b = self.b * r.b

        return Rational(a, b)

    __radd__ = __add__

    def __sub__(self, r):
        if isinstance(r, int):
            a = r * self.b - self.a
            b = self.b
        else:
            a = self.a * r.b - self.b * r.a
            b = self.b * r.b

        return Ratioanal(a, b)

    __rsub__ = __sub__

    def __mul__(self, r):
        if isinstance(r, int):
            a = self.a * r
            b = self.b
        else:
            a = self.a * r.a
            b = self.b * r.b

        return Rational(a, b)

    __rmul__ = __mul__

    def __truediv__(self, r):
        if isinstance(r, int):
            a = self.a
            b = self.b * r
        else:
            a = self.a * r.b
            b = self.b * r.a
            
        return Rational(a, b)

    __rtruediv__ = __truediv__
            

    def __lt__(self, r):
        if isinstance(r, int):
            return self.a / self.b < r
        
        return self.a / self.b < r.a / r.b

    def __le__(self, r):
        if isinstance(r, int):
            return self.a / self.b <= r
        
        return self.a / self.b <= r.a / r.b

    def __gt__(self, r):
        if isinstance(r, int):
            return self.a / self.b > r
        
        return self.a / self.b > r.a / r.b

    def __ge__(self, r):
        if isinstance(r, int):
            return self.a / self.b >= r
        
        return self.a / self.b >= r.a / r.b

    def __eq__(self, r):
        if isinstance(r, int):
            return self.a / self.b == r
        
        return self.a / self.b == r.a / r.b

    def __ne__(self, r):
        if isinstance(r, int):
            return self.a / self.b != r
        
        return self.a / self.b >= r.a != r.b

    def __float__(self):
        return self.a / self.b
    
    def __int__(self):
        return self.a // self.b
    
    def __bool__(self):
        return self.a != 0

x = Rational(3, 2)
y = Rational(1, 2)

result = x + y * x
print(result)

result = x / 2
print(result)

result = float(x)
print(result)

result = int(x)
print(result)

z = Rational()
if z:
    print('Doğru')
else:
    print('Yanlış')

if x > y:
    print('x > y')
elif x < y:
    print('x < y')
elif x == y:
    print('x == y')
