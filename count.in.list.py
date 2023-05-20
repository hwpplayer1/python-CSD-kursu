a = [1, 2, 2, 3, 4, 5, 2, 1, 2, 3, 1, 2]
val = int(input('Aranacak değeri giriniz:'))

count = 0
for i in a:
    if i == val:
        count += 1
print(count)
