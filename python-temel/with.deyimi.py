class Sample:
    def __init__(self):
        print('__init__ called')

    def __enter__(self):
        print('__enter__ called')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ called')
        return False

print('begins...')
with Sample() as s:
    print('suite')
print('ends...')
