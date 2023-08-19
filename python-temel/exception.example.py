while True:
    try:
        val = int(input('Bir değer giriniz:'))
        break
    except ValueError:
        print('Geçersiz bir değer girdiniz!')

print(val * val)
