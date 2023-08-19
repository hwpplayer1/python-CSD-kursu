try:
    val = int(input('Bir değer giriniz:'))
    print(val * val)
except TypeError:
    print('Girilen değerin türü uygun değil!')
except:
    print('Diğer bir nedenden dolayı exception oluştu')
