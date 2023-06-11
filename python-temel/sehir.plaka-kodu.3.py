cities = [('ankara', 6), ('izmir', 35), ('eskişehir', 26), ('muğla', 48), ('kastamonu', 37)]
s = ['{}-{}'.format(*city) for city in cities]
print(s)
