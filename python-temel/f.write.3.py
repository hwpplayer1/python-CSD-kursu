with open('test.txt', 'w') as f:
    while True:
        s = input('Bir yazı giriniz:')
        if s == 'çık':
            break
        f.write(s + '\n')
