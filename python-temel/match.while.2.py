while True:
    cmd = input('CSD>').strip()
    match cmd:
        case 'delete' | 'remove' | 'erase' as x:
            print(f'silme işlemi "(x)" komutu ile yapılıyor')
        case 'copy':
            print('kopyalama işlemi')
        case 'rename':
            print('isim değiştirme işlemi')
        case 'exit' | 'quit':
            break
        case _:
            print('geçersiz komut!')