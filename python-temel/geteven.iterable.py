def geteven(iterable):
    for x in iterable:
        if x % 2 == 0:
            yield x

l = [2, 5, 7, 8, 4]
for i in geteven(l):
    print(i, end=' ')
print()

