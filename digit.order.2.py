n = int(input('Bir sayı giriniz:'))

digits = []
while n > 0:
    r = n % 10
    digits.append(r)
    n //= 10

for digit in reversed(digits):
    print(digit, end=' ')
