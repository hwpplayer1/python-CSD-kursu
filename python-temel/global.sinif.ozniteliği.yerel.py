x = 100

class Sample:
    x = 200
    def foo(self):
        x = 300
        print(x)          # 300
    print(x)              # 200
print(x)                  # 100

s = Sample()
s.foo()
