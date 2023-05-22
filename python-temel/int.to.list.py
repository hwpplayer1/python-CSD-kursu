s = input('Liste değerlerini aralarına boşluk karakterleri koyarak giriniz:')
a = []
for s in s.split():
    a.append(int(s))
print(a)
