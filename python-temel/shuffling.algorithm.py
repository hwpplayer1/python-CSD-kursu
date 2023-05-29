import random

def myshuffle(sequence):
    for i in range(len(sequence)):
        k = random.randrange(len(sequence))
        sequence[i], sequence[k] = sequence[k], sequence[i]

a = list(range(10))
print(a)
myshuffle(a)
print(a)
