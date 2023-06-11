cities = ['ankara', 'adana', 'izmir', 'bolu', 'çanakkale', 'amasya']
xcities = [city[:3].upper() for city in cities if 'a' in city.lower()]
print(xcities)
