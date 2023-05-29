import random

def create_deck():
    types = ('Sinek', 'Maça', 'Karo', 'Kupa')
    numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Vale', 'Kız', 'Papaz', 'As')

    deck = []
    for number in numbers:
        for type in types:
            deck.append(type + '-' + number)
    return deck

deck = create_deck()
print(deck)
random.shuffle(deck)
print(deck)
