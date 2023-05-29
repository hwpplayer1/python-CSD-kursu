import random

def create_deck():
    types = ('Sinek', 'Maça', 'Karo', 'Kupa')
    numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Vale', 'Kız', 'Papaz', 'As')

    deck = []
    for number in numbers:
        for type in types:
            deck.append(type + '-' + number)
    return deck

def distribute_deck(deck):
    cards = ([],  [], [], [])

    for i in range(len(deck)):
        cards[i % 4].append(deck[i])
    return cards

deck = create_deck()
random.shuffle(deck)
print(deck)

north, east, south, west = distribute_deck(deck)
print(north)
print(east)
print(south)
print(west)
