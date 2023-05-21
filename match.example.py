a = int(input('bir değer giriniz:'))

match a:
    case 1:
        print('bir')
    case 2:
        print('iki')
    case 3:
        print('üç')
    case 4:
        print('dört')
    case 5:
        print('beş')
    case _:
        print('hiçbiri')
