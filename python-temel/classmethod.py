class Sample:
    def __init__(self):                       # örnek metodu
        self.a = 10

    @staticmethod
    def bar():                                # statik metot
        print('bar')

    @classmethod                              # sınıf metodu
    def tar(cls):
        print('tar')
        
