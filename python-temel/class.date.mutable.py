class Date:
    def set(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def disp(self):
        print('{}/{}/{}'.format(self.day, self.month, self.year))

date = Date()
date.set(10, 12, 1990)
date.disp()
