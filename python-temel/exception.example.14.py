class MyError(Exception):
    pass

try:
    a = int(input('Bir değer giriniz:'))
    if a < 0:
        raise MyError()
    print(a * a)
except ValueError:
    print('Girilen değer geçersiz!')
except MyError:
    print('Sayı negatif!')
print('ends...')
