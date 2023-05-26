import random

def get_random(a, b, size):
    result = []
    if isinstance(size, int):
        for i in range(size):
            result.append(random.randint(a, b - 1))
    elif isinstance(size, tuple):
        if len(size) != 2:
            raise TypeError('tuple must have 2 elements!')
        for i in range(size[0]):
            col = []
            for k in range(size[1]):
                col.append(random.randint(a, b - 1))
                result.append(col)
    else:
        raise TypeError('invalid type!')
    return result

x = get_random(0, 10, 5)
print(x)

y = get_random(0, 10, (5, 4))
print(y)
