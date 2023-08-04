import datetime as dt

def mylog(f):
    file = open('logfile.txt', 'w')
    def log():
        file.write('function called at ' + str(dt.datetime.now()) + '\n')
        f()
    return log

@mylog
def foo():
    print('foo')

foo()
foo()
foo()
