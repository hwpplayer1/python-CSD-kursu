cities = ['ankara', 'izmir', 'eskişehir', 'muğla', 'kastamonu']
charList = [ch for city in cities for ch in city]
s = set(charList)
print(s)
