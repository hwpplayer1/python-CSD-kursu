class Sample:
    def __call__(self, x, y):
        print('call: {}, {}'.format(x, y))
        return x + y

s = Sample()
result = s(10, 20)
print(result)

