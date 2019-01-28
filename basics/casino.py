import random


class Deck(object):
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " of " + suit)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


d = Deck()
d.shuffle()
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())