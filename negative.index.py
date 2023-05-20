a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(a) // 2:
    a[i], a[-i -1] = a[-i -1], a[i]
    i += 1
print(a)
