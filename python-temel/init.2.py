class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 1900

    def disp(self):
        print('{}/{}/{}'.format(self.day, self.month, self.year))

date = Date() 
date.disp()                           # Date.disp(date)
