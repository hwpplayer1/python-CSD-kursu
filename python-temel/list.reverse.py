a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
lena = len(a)
while i < lena //  2:
    a[i], a[lena -1 -i] = a[lena -1 -i], a[i]
    i += 1
print(a)
