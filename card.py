from constants import SUITS, RANKS

class Card:

    def __init__(self, suit, rank):
        """ 
        Constructor for Card class
        """
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        """ Returns a string
        Suit of a card
        """
        return self.suit

    def getRank(self):
        """ Returns a string
        Rank of a card
        """
        return self.rank

    def __str__(self):
        """ Returns a string
        Formatted string of a card
        """
        return self.rank + ' of ' + self.suit