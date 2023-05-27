def add(*a):
    total = 0
    for x in a:
        if isinstance(x, (list, tuple)):
            total += sum(x)
        else:
            total += x
    return total

x = [20, 30]
result = add(10, x, 40)
print(result)
