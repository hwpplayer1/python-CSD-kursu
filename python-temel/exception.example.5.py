try:
    val = int(input('Bir değer giriniz:'))
    print(val * val)
except TypeError:
    print('Girilen değerin türü uygun değil!')
except:
    print('Diğer bir nedenden dolayı exception oluştu')
else:
    print('else bölümü yalnızca exception oluşmadığı zaman çalıştırılır...')
print('Bu deyim her zaman çalıştırılacaktır')
