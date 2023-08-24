d = dict()
with open('test.csv', 'r') as f:
    for line in f:
        if line.strip() == '':
            continue
        l = line.split(',')
        d[l[0]] = l[1].strip()
        print(d)
