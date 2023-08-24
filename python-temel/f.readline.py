with open('sample.py', 'r') as f:
    while True:
        s = f.readline()
        if s == '':
            break
        print(s, end='')
