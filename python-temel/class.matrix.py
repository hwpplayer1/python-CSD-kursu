class Matrix:
    def __init__(self, nrows, ncols):
        self.matrix = [[0] * ncols for i in range(nrows)]

    def __getitem__(self, index):
        return self.matrix[index[0]][index[1]]

    def __setitem__(self, index, val):
        self.matrix[index[0]][index[1]] = val

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                if k != 0:
                    s += ' '
                s += str(self.matrix[i][k])
            s += '\n'

        return s

m = Matrix(5, 5)

for i in range(5):
    for k in range(5):
        m[i, k] = i + k

for i in range(5):
    for k in range(5):
        print(m[i, k], end=' ')
    print()

print()
print(m)
