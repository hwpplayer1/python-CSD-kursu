a = [10, 13, 8, 22, 64, 73]

for index, val in enumerate(a):
    if val % 2 == 1:
        a[index] += 1

print(a)
