a = [23, 56, 44, 12, 13, 97, 45, 39, 80, 54]
odd = []
even = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)
