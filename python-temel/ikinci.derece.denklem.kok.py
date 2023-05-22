import math

def disp_roots(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'x1 = {x1}, x2 = {x2}')
    else:
        print('kök yok')

disp_roots(1, 0, -4)
