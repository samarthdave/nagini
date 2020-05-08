##########################################
##### A Deck of Cards made in Python #####
##########################################

from random import shuffle

# a Card (has suit & value)
class Card:
    # all possible suits, build a set from it
    _suits_list = ("Hearts", "Diamonds", "Clubs", "Spades")
    _suits_set = set(_suits_list)
    # all possible numerical values
    _ranks_list = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    _ranks_set = set(_ranks_list)
    
    def __init__(self, rank, suit):
        if suit not in self._suits_set:
            raise ValueError("Invalid suit: {}".format(suit))
        if rank not in self._ranks_set:
            raise ValueError("Invalid rank: {}".format(rank))
        # Generate an Ace of Spades by default
        self._suit = suit
        self._rank = rank
    
    def __repr__(self):
        # returns "J of Diamonds"
        return "{} of {}".format(self._rank, self._suit)

#####################
## a deck of Cards ##
#####################
class Deck:

    def __init__(self):
        # build all 52 cards w/ a list comprehension
        self.cards = [Card(rank, suit) for suit in Card._suits_list
                                       for rank in Card._ranks_list]
        #####################################
        # a (not so Pythonic) way of doing it:
        # for suit in Card._suits_list:
        #     for rank in Card._ranks_list:
        #         # add the card to the deck
        #         self.cards.append(Card(rank, suit))

    def count(self):
        return len(self.cards)

    def __repr__(self):
        card_count = len(self.cards)
        return "Deck of {} cards".format(self.count())
    
    # deal N cards
    def _deal(self, num):
        count = self.count()
        actual = min(count, num)

        if count == 0:
            raise ValueError("All cards have been dealt")

        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]

        print('Dealing {} cards'.format(actual))
        return cards
    
    # deals one card
    def deal_card(self):
        return self._deal(1)[0]
    
    # deal a hand
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only standard decks can be shuffled")

        shuffle(self.cards)
        return self
    
    # override standard shuffle procedure
    def non_standard_shuffle(self):
        count = self.count()
        if count != 52:
            print("Warning: Shuffling {} cards".format(count))
        shuffle(self.cards)
        return self
    
d = Deck()

d.shuffle()