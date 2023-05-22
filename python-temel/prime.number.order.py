n = int(input('Bir sayı giriniz:'))
div = 2
while n != 1:
    if n % div == 0:
        n //= div
        print(div, end=' ')
    else:
        div += 1
