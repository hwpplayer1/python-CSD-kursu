class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return 'Date object: {}/{}/{}'.format(self.day, self.month, self.year)

d = Date(10, 12, 2008)
print(d)                             # Date object: 10/12/2008
print(str(d))                        # Date object: 10/12/2008
print(repr(d))                       # Date object: 10/12/2008
