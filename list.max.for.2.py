a = [3, 5, 7, 9, 21, 10, 62, 34, 9, 5, 8]

maxval = a[0]
for i in a[1:]:
    if i > maxval:
        maxval = i

print(maxval)
