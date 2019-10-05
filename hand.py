from constants import SUITS, RANKS

class Hand:

    def __init__(self):
        """ 
        Constructor for Hand class
        """
        self.cards = []
        self.value = 0
        self.has_ace = False

    def __str__(self):
        """ Returns a string
        Formatted string of a hand
        """
        return ", ".join(str(card) for card in self.cards)
    
    def addCard(self, card):
        """ Returns void
        Adds an instance of Card to the list of cards
        """
        self.cards.append(card)
        rank = card.getRank()
        self.value += RANKS[rank]
        self.has_ace |= (rank == "ACE")  

    def getValue(self):
        """ Returns an integer
        Returns the value of the hand
        """
        if self.value < 12 and self.has_ace:
            return self.value + 10
         
        return self.value

    def canSplit(self):
        """ Returns a boolean
        Checks if first two cards in the hand have the same rank
        """
        if len(self.cards) == 2:
            return RANKS[self.cards[0].getRank()] == RANKS[self.cards[1].getRank()]
        return False
    
    def getCard(self, idx):
        """ Returns an instance of type Card
        Returns the card at a specified valid index
        """
        if 0 <= idx < len(self.cards):
            return self.cards[idx]
        return None