with open('test.txt', 'r') as f:
    while True:
        s = f.read(5)
        if s == '':
            break
        print(s, end='')
