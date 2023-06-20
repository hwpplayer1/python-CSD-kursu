import datetime as dt
s = input('Tarih giriniz:')
day, month, year = [int(k) for k in s.split('/')]

d = dt.date(year, month, day)
day_text = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
print(day_text[d.weekday()])
