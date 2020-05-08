##########################################
##### A Deck of Cards made in Python #####
##########################################

from random import shuffle

# a Card (has suit & value)
class Card:
    # all possible suits, build a set from it
    _suits_list = ("Hearts", "Diamonds", "Clubs", "Spades")
    _card_set = set(_suits_list)
    # all possible numerical values
    _ranks_list = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    _rank_set = set(_ranks_list)
    
    def __init__(self, rank, suit):
        # Generate an Ace of Spades by default
        self._suit = suit if suit in self._card_set else "Hearts"
        self._rank = rank if rank in self._rank_set else "A"
    
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
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

d = Deck()

d.shuffle()