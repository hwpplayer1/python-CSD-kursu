import datetime

d = datetime.date(1920, 4, 23)
print('{}/{}/{}'.format(d.day, d.month, d.year))
days = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi']

wd = d.weekday()
print(days[wd])
