s = 'ağrı dağı çok yüksek'
with open('test.dat', 'wb') as f:
    b = bytes(s, encoding='utf-8')
    f.write(b)
