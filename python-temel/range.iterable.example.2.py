r = range(10)
for i in r:
    print(i, end = ' ')
print()

r = range(10)
iter = r.__iter__()
try:
    while True:
        i = iter.__next__()
        print(i, end = ' ')
    print()
except StopIteration:
    pass
print()
