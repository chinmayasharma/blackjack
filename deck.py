from card import Card
from constants import SUITS, RANKS
import random

class Deck:
    
    def __init__(self):
        """ 
        Constructor for Deck class
        """
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    # randomly shuffles the deck 
    def shuffle(self):
        """ Returns void
        Shuffles a given deck
        """
        random.shuffle(self.cards)

    # deals a single card from the deck 
    def dealCard(self):
        """ Returns an instance of type Card
        Removes a card from a given deck and returns it
        """
        return self.cards.pop(0)