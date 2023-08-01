class MyList:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, key):
        return self.array[key]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)

ml = MyList([10, 20, 30, 40])

for i in range(len(ml)):
    ml[i] = ml[i] * 2

print(ml)
