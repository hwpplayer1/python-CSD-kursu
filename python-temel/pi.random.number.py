import random
import math

def getpi(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x ** 2 + y ** 2) < 1:
            count += 1
    return 4 * count / n

while True:
    n = int(input('Bir sayı giriniz:'))
    if n == 0:
        break
    pi = getpi(n)
    print(pi)
