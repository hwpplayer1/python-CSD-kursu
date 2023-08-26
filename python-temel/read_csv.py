def read_csv(path, converters=None, header=False):
    with open(path) as f:
        if header:
            h = f.readline()[:-1].split(',')
        l = []
        for line in f:
            a = line[:-1].split(',')
            if a[0] == '':
                continue
            if converters:
                for key, value in converters.items():
                    a[key] = value(a[key])
            l.append(a)

    if header:
        return l, h

    return l

l, h = read_csv('people.csv', None, True)

print(l)
print(h)
