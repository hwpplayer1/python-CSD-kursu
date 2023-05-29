import random

def get_column():
    result = []
    numbers = list(range(1, 50))
    for i in range(6):
        x = random.choice(numbers)
        result.append(x)
        numbers.remove(x)
    return result

column = get_column()
print(column)
