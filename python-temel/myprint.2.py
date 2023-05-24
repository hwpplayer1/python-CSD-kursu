def myprint(*Objects, sep = ' ', end = '\n'):
    if len(Objects) == 0:
        print(end = end)
        return
    for obj in Objects[::-1]:
        print(obj, end=sep)
    print(Objects[-1], end=end)

myprint(10, 20)
myprint(30, 40)
myprint(10, 20, 30, sep = ',')
