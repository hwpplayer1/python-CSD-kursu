class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year):
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

result = Date.is_leap_year(2000)
print('Artık' if result else 'Artık değil')
