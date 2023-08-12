try:
    s = input('Bir değer giriniz:')
    x = int(s)
    print(x)
except ValueError:
    print('Girilen değer geçersiz!')
print('Program sonlanıyor...')
