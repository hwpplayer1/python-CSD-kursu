def foo():
    a = 10
    d = locals()
    d['b'] = 100

    print(b)

foo()

# Burada biz b değişkenini foo fonksiyonunun yerel değişken listesine ekleyemedik. Bu nedenle print çağrısında error oluşacaktır.
