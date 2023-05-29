a = [12, 34, 2, 78, 4, 30, -9, 44, 88, 41, 20]

mi = 0
for i, x in enumerate(a):
    if x > a[mi]:
        mi = i

print(f'En büyük eleman: {a[mi]}, indeksi: {mi}')
