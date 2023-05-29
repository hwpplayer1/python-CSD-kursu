import random

def coin(n):
    head = tail = 0
    for i in range(n):
        x = random.randint(0, 1)
        if x == 0:
            tail += 1
        else:
            head += 1
    return head / n, tail / n

head, tail = coin(1000000)
print(f'tura: {head}, yazı: {tail}')
