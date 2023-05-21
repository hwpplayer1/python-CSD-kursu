a = [23, 45, 34, 67, 89, 34, 56, 11, 23, 45]
val = int(input('Aranacak sayıyı giriniz:'))
for i in a:
    if i == val:
        print('bulundu')
        break
if i != val:
    print('bulunamadı')
