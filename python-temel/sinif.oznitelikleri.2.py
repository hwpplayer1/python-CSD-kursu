x = 10             # x bir global değişken

class Sample:
    print(x)       # geçerli global x
    x = 20         # yeni bir sınıf değişkeni olan x yaratılıyor

print(x)           # 10
print(Sample.x)    # 20
print(x)           # 10
