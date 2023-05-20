a = [3, 5, 7, 9, 21, 10, 62, 34, 9, 5, 8]

maxval = a[0]
for i in range(1, len(a)):
    if a[i] > maxval:
        maxval = a[i]

print(maxval)
