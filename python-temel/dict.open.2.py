with open('test.2.csv') as f:
    a = []
    for line in f:
        a.append(line[:-1].split(','))
print(a)
