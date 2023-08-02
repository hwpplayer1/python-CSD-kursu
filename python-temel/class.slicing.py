class MyArray:
    def __init__(self, a):
        self.a = a

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self.a[i] for i in range(*index.indices(len(self.a)))] # return
        self.a[index]
        return self.a[index]

    def __setitem__(self, index, val):
        if isinstance(index, slice):
            k = 0
            for i in range(*index.indices(len(self.a))):
                self.a[i] = val[k]
                k += 1
        else:
            self.a[index] = val

    def __len__(self):
        return len(self.a)

    def __str__(self):
        return str(self.a)

ml = MyArray([10, 20, 30, 40, 50])
result = ml[3:5]
print(result)

result = ml[3]
print(result)

ml[3:5] = [100, 200]
print(ml)

ml[3] = 300
print(ml)


