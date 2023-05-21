while True:
    cmd = input('CSD>').split()
    match cmd:
         case 'delete', path, *others:
             print(f'delete{path} {others}')
         case _:
             print('geçersiz komut!')
