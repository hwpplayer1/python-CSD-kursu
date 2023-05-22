for i in range(5):
    val = int(input('Bir değer giriniz:'))
    if val == 0:
        break
    print(val * val)
else:
    print('Döngü sonlandı')
print('Program sonlandı')
