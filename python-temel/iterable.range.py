r = range(10)

iterator = r.__iter__()

for x in iterator:
    print(x, end=' ')

print()

for x in iterator:
    print(x, end=' ')
