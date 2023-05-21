while True:
    cmd = input('CSD>').strip()
    match  cmd:
         case 'delete' | 'remove'   'erase':
             print('silme işlemi')
         case 'copy':
             print('kopyalama işlemi')
         case 'rename':
             print('isim değiştirme işlemi')
         case 'exit'  |  'quit':
             break
         case _:
             print('geçersiz komut!')
