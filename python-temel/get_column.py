import random

def get_column():
    result = []
    for i in range(6):
        while True:
            val = random.randint(1, 49)
            if val not in result:
                break
        result.append(val)
    return result

col = get_column()
for i in col:
    print(i, end = ' ')
