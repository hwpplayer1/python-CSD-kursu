with open('sample.py', 'r') as f:
    while (s := f.readline()) != '':
        print(s, end='')
