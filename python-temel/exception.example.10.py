def bar(a):
    print('bar başladı')
    if a < 0:
        raise ValueError('Argüman negatif olamaz')
    print('bar bitti')

def foo(a):
    print('foo başladı')
    try:
        bar(a)
    except Exception as e:
        print(f"Exception foo'da ele alındı ve yeniden fırlatılıyor: {e}")
        raise
    print('foo bitti')
try:
    foo(-10)
except Exception as e:
    print(f'Exception dışarıda ele alındı: {e}')
