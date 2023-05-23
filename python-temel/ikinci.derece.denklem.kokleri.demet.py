import math

def getroots(a, b, c):
    delta = b * b - 4 * a * c
    if delta <= 0:
        return None
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)

    return x1, x2

def main():
    a = float(input('a:'))
    b = float(input('b:'))
    c = float(input('c:'))

    result = getroots(a, b, c)
    if result == None:
        print('Kök yok')
    else:
        x1, x2 = result
        print('x1 = {}, x2 = {}'.format(x1, x2))

main()
