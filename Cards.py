class Card():
    """Just a card"""

    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # ♠ ♦ ♣ ♥
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand:
    """A hand is a composition of cards of a player"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
            return rep
        
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

card1 = Card(rank = "A", suit = Card.SUITS[0])
print("Deducing card-object on the screen")
print(card1)

card2 = Card(rank = "2", suit = Card.SUITS[0])
card3 = Card(rank = "3", suit = Card.SUITS[0])
card4 = Card(rank = "4", suit = Card.SUITS[0])
card5 = Card(rank = "5", suit = Card.SUITS[0])
print("\nDEDUCING 4 CARDS MORE:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nPrinting cards before giveaway")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nPrinting 5 cards which appeared in  my hand:")
print(my_hand)
