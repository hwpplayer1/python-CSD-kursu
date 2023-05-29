import random

def getrand(a, b, count):
    l = []
    for i in range(count):
        val = random.randint(a, b)
        l.append(val)
    return l

a = getrand(0, 99, 5)
print(a)
