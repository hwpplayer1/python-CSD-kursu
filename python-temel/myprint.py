def myprint(*Objects, sep = ' ', end = '\n'):
    i = 0
    while i < len(Objects):
        if i != 0:
            print(sep, end='')
        print(Objects[i], end='')
        i += 1
    print(end = end)

myprint(10, 20)
myprint(30, 40)
myprint(10, 20, 30, sep=',')
