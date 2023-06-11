cities = ['ankara', 'adana', 'izmir', 'bolu', 'çanakkale', 'amasya']
xcities = [city[:3].upper() for city in cities if city.lower().find('a') != -1]
print(xcities)
