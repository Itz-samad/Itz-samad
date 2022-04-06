Cards = ['1c', '2c', '3c', '4c', '5c', '7c', '8c', '10c', '11c', '12c', '13c', '14c', '1cr', '2cr', '3cr', '4cr', '5cr',
         '7cr', '8cr', '10cr', '11cr', '12cr', '13cr', '14cr', '1st', '2st', '3st', '4st', '5st', '7st', '8st', '10st',
         '11st', '12st', '13st', '14st', '1t', '2t', '3t', '4t', '5t', '7t', '8t', '10t', '11t', '12t', '13t', '14t',
         '1s', '2s', '3s', '4s', '5s', '7s', '8s', '10s', '11s', '12s', '13s', '14s', 'Whot', 'Whot', 'Whot', 'Whot']


class Deck(object):
    def __init__(self):
        self.cards = []

    def populate(self, cards: list):
        self.cards = cards
        print('Stacking the deck .... \n Deck has been stacked successfully')

    def shuffle(self):
        import random
        random.shuffle(self.cards)
        print('Shuffled successfully ....')

    def share(self):
        import random
        hands = []
        counter = 0
        while counter <= 4:
            if self.cards:
                while counter <= 4:
                    m = random.randint(0, 60)
                    self.m = m
                    hands.append(self.cards[m])
                    counter += 1


            else:
                print('na')
        print(hands)
        self.hands = hands
        return hands

    def gen_mark(self):
        for element in self.hands:
            if element in self.cards:
                self.cards.remove(element)

            else:
                print('na')
        print(self.cards)

    def show_hand(self):
        print(self.hands)


class Hand(object):
    def __init__(self, cad: list):
        self.cad = cad

    def new(self):
        print(self.cad)


def whot():
    global mine
    print("Welcome to the game of wot")
    c1 = Deck()
    while 1 <= 2:
        b = input('\nPress:'
                  ' \n Q - Stack the deck \n\n R - Shuffle the cards \n\n G - Share the cards  '
                  '\n\n I - Show market \n\n E - Show hand')
        if b.upper() == 'Q':
            c1.populate(Cards)
        elif b.upper() == 'R':
            c1.shuffle()
        elif b.upper() == 'G':
            c1.populate(Cards)
            mine = Hand(c1.share())
        elif b.upper() == 'I':
            c1.gen_mark()
        elif b.upper() == 'E':
            mine.new()


whot()

# Carda = ['1c', '2c', '3c', '4c', '5c', '7c', '8c', '10c', '11c', '12c', '13c', '14c', '1cr', '2cr', '3cr', '4cr',
#              '5cr', '7cr', '8cr', '10cr', '11cr', '12cr', '13cr', '14cr', '1st', '2st', '3st', '4st', '5st', '7st',
#              '8st', '10st', '11st', '12st', '13st', '14st', '1t', '2t', '3t', '4t', '5t', '7t', '8t', '10t', '11t',
#              '12t', '13t', '14t', '1s', '2s', '3s', '4s', '5s', '7s', '8s', '10s', '11s', '12s', '13s', '14s', 'Whot',
#              'Whot', 'Whot', 'Whot']
# class Card(object):
#     """ A playing card. """
#     Cards = ['1c', '2c', '3c', '4c', '5c', '7c', '8c', '10c', '11c', '12c', '13c', '14c', '1cr', '2cr', '3cr', '4cr',
#              '5cr', '7cr', '8cr', '10cr', '11cr', '12cr', '13cr', '14cr', '1st', '2st', '3st', '4st', '5st', '7st',
#              '8st', '10st', '11st', '12st', '13st', '14st', '1t', '2t', '3t', '4t', '5t', '7t', '8t', '10t', '11t',
#              '12t', '13t', '14t', '1s', '2s', '3s', '4s', '5s', '7s', '8s', '10s', '11s', '12s', '13s', '14s', 'Whot',
#              'Whot', 'Whot', 'Whot']
#
#     def __init__(self, cad):
#         self.cad = cad
#
#     def __str__(self):
#         rep = str(self.cad)
#         return rep
#
#
# class Hand(object):
#     """ A hand of playing cards. """
#
#     def __init__(self):
#         self.cards = []
#
#     def __str__(self):
#         if self.cards:
#             rep = ""
#             for card in self.cards:
#                 rep += str(card) + "\t"
#         else:
#             rep = "<empty>"
#             return rep
#
#     def clear(self):
#         self.cards = []
#
#     def add(self, card):
#         self.cards.append(card)
#
#     def give(self, card, other_hand):
#         self.cards.remove(card)
#         other_hand.add(card)
#
#
# class Deck(Hand):
#     def populate(self):
#         for cad in Card.Cards:
#             for rank in cad:
#                 self.add(rank)
#
#     def shuffle(self):
#         import random
#         random.shuffle(self.cards)
#
#     def deal(self, hands):
#         for rounds in range(4):
#                 if self.cards:
#                     top_card = self.cards[0]
#                     self.give(top_card, hand)
#         else:
#             print("Can't continue deal. Out of cards!")
#
#
# cada = Card(Carda)
# deck1 = Deck()
# deck1.populate()
# print(cada)
# for each in print(cada:
#     print(each)
