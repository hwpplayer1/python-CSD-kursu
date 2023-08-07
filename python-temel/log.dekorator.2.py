import datetime
import time

def log(path):
    file = open(path, 'w')
    def bar(f):
        def tar(*args, **kwargs):
            dt = datetime.datetime.now()
            print(dt)
            file.write(str(dt) + '\n')
            f(*args, **kwargs)
        return tar
    return bar

@log('log.txt')
def foo():
    print('foo çağrıldı')

foo()
time.sleep(3)
foo()
time.sleep(2)
foo()
