with open('test.2.csv') as f:
    a = [line[:-1].split(',') for line in f]
print(a)
