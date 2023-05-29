a = [23, 56, 12, 34, 8, 21, 16, 43]

index = 0
for i in range(1, len(a)):
    if a[i] > a[index]:
        index = i

print(f'En büyük elaman: {a[index]}, indeksi: {index}')
