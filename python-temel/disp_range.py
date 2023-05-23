def disp_range(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0

    for i in range(start, stop, step):
        print(i, end=' ')

disp_range(10)
disp_range(2, 8)
disp_range(2, 8, 3)
