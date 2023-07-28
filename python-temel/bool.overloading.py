class Number:
    def __init__(self, number):
        self.number = number

    def disp(self):
        print(self.number)

    def __eq__(self, x):
        return self.number == x.number

    def __ne__(self, x):
        return self.number != x.number

    def __gt__(self, x):
        return self.number > x.number

    def __lt__(self, x):
        return self.number < x.number

    def __ge__(self, x):
        return self.number >= x.number

    def __le__(self, x):
        return self.number <= x.number


n = Number(10)
k = Number(10)

if n == k:
    print('Evet')
else:
    print('Hayır')
