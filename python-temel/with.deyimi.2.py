class FileWrapper:
    def __init__(self, path):
        self.f = open(path, 'w')

    def write(self, s):
        self.f.write(s)

    def close(self):
        self.f.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()
        return False

try:
    with FileWrapper('test.txt') as f:
        f.write('this is a test')
    #....
except:
    print('file io error!')

# Bu noktada dosya kapatılmış olacak
