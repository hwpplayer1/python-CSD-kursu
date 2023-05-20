import math
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

delta = b * b - 4 * a * c
if delta < 0:
    print('Kök yok')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('x1 = {}, x2 = {}'.format(x1, x2))
