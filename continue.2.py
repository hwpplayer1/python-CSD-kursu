while True:
    cmd = input('CSD>').strip()
    if cmd == '':
        continue
    if cmd == 'dir':
        print('dir command')
    elif cmd == 'del':
        print('del command')
    elif cmd == 'copy':
        print('copy command')
    elif cmd == 'exit':
        break
    else:
        print('bad command')
