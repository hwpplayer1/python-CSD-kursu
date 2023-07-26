class Sample:
    def __del__(self):
        print('Nesne yok edilecek!')

s = Sample()
print('Referans sayacı 1')
k = s
print('Referans sayacı 2')

k = None
print('Referans sayacı 1')
s = None
print('Referans sayacı 0')
