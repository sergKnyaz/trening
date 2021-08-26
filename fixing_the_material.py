class Card(object):
    RANG = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUIT = ['v', 'h', 's', 'f']

    def __init__(self, rang, suit):
        self.rang = rang
        self.suit = suit

    def __str__(self):
        rep = self.rang + self.suit
        return rep


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ''
        if self.cards:
            for card in self.cards:
                rep += str(card) + ' '
        else:
            rep = '<у меня нет карт>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, oter_hand):
        self.cards.remove(card)
        oter_hand.add(card)


# class Deck(Hand):
#     def populate(self):
#         self.cards = []
#         for suit in Card.SUIT:
#             for rang in Card.RANG:
#                 self.cards.append(Card(rang, suit))
#
#     def shuffle(self):
#         import random
#         random.shuffle(self.cards)
#
#     def deal(self, hands, per_hand=0):
#         for rounds in range(per_hand):
#             for hand in hands:
#                 if self.cards:
#                     top_card = self.cards[0]
#                     self.give(top_card, hand)
#
#
#
# hand1 = Hand()
# hand2 = Hand()
# hand3=Hand()
# hand4=Hand()
#
# print(hand1)
# print(hand2)
#
# deck = Deck()
# deck.populate()
# print(deck)
# deck.shuffle()
# print(deck)
# hands = [hand1, hand2,hand3,hand4]
# deck.deal(hands, per_hand=6)
# print(hand1)
# print(hand2)
# print(hand3)
# print(hand4)
# print(deck)
