s = input('Bir renk giriniz:')

match s:
    case 'kırmızı':
        print('red')
    case 'mavi':
        print('blue')
    case 'yeşil':
        print('üç')
    case 4:
        print('green')
    case _:
        print('another color')
    
