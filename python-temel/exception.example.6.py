try:
    val = int(input('Bir değer giriniz:'))
    print(val * val)
    print('else bölümü yalnızca exception oluşmadığı zaman çalıştırılır...')
except TypeError:
    print('Girilen değerin türü uygun değil!')
except:
    print('Diğer bir nedenden dolayı exception oluştu')
print('Bu deyim her zaman çalıştırılacaktır')
