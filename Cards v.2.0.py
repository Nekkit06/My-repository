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

class Deck(Hand):
    """Deck of cards"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("I can't give any more cards:"),
                    "no more cards!"


#main
deck1 = Deck()
print("New deck created.")
print("Here it is:")
print(deck1)

deck1.populate()
print("\nNew cards appeared in the deck.")
print("This is how it looks now:")
print(deck1)

deck1.shuffle()
print("\nDeck shuffled.")
print("This is how it looks now:")
print(deck1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand = 5)
print("\nWe've been given 5 cards")
print("My hand is:")
print(my_hand)
print("Your hand is:")
print(your_hand)
print("Left in deck:")
print(deck1)
