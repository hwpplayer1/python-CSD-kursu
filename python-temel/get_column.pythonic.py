import random

def get_column():
    result = set()
    while len(result) != 6:
        val = random.randint(1, 49)
        result.add(val)
    return list(result)

col = get_column()
for i in col:
    print(i, end = ' ')
