with open('test.txt', 'r+') as f:
    f.seek(0, 2)
    s = f.write('xxx')
