import sys

class Sample:
    def __del__(self):
        print('__del__ called')

a = Sample()
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
c = b
print(sys.getrefcount(a))
c = None
print(sys.getrefcount(a))
b = None
print(sys.getrefcount(a))
a = None
