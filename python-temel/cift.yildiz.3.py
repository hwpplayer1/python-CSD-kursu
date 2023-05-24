def printmsg(s, **d):
    count = d.get('count')
    if count == None:
        count = 1

    print(s * count)

printmsg('ok', count = 4)
