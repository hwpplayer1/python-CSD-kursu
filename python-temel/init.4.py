class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def disp(self):
        print('{}/{}/{}'.format(self.day, self.month, self.year))

date = Date(10, 12, 2009)
date.disp()                         # Date.disp(date)
