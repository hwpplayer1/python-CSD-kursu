n =  int(input('Bir sayı giriniz:'))

for i in range(2, n):
    if n % i == 0:
        print('Asal değil')
        break
else:
    if n < 2:
        print('Gecersiz sayı!')
    else:
        print('Asal')
