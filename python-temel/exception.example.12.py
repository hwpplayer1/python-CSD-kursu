def foo():
    print('foo begins...')
    try:
        while True:
            a = int(input('Bir değer giriniz:'))
            if a == 0:
                return
            print(a * a)
    except:
        print('Exception oluştu!..')
    finally:
        print('finally!..')
foo()
