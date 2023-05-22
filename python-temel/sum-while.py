a = [3, 4, 3, 5, 10]
total = 0
i = 0
while i < len(a):
    total += a[i]
    i += 1
avg = total / len(a)
print('Ortalama =', avg)