x = 10

def foo():
    y = 20
    print(y)                      # 20

class Sample:
    def bar(self):
        z = 30                    # 30
        print(z)

foo()
s = Sample()
s.bar()
print(x)                          # 10
