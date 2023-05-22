while True:
    cmd = input('CSD>').split()
    match cmd:
         case ('delete', path)  | ('remove', path) | ('erase', path):
             print(f'{path} dosyası siliniyor')
         case 'copy', source_path, dest_path:
             print(f'{source_path} dosyası {dest_path} olarak kopyalanıyor')
         case 'rename', oldname, newname:
             print(f'{oldname} dosyasının ismi {newname} olarak değiştiriliyor')
         case 'exit' | 'quit':
             break
         case _:
             print('geçersiz komut!')
