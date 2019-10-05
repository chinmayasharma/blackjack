from card import Card
from hand import Hand
from constants import SUITS, RANKS, Color

# print string with colors
def printColored(cards, color):
    return color + cards.__str__() + Color.END

def printStatus(upcard, player):
    print("Dealer's Face-Up Card: " + printColored(upcard, Color.CYAN))
    print("Player's Hand: " + printColored(player, Color.YELLOW))

def findWinner(deck, player, dealer, balance, wager):
    player_value = player.getValue()
    print("Dealer's hands: " + printColored(dealer, Color.CYAN))
    
    if player_value > 21:
        print("Player got: %s and goes bust. Dealer Wins!" %player_value)
        balance -= wager
    
    else:
        while dealer.getValue() < 17: 
            dealer.addCard(deck.dealCard())
            print("Dealer's hands: " + printColored(dealer, Color.CYAN))

        dealer_value = dealer.getValue()

        if dealer_value > 21:
            print("Dealer got: %s and goes bust. Player Wins!" %dealer_value)
            balance += wager

        elif player_value > dealer_value:
            print("Player got: %s, Dealer got: %s. Player Wins!" %(player_value, dealer_value))
            balance += wager

        elif player_value == dealer_value:
            print("Player got: %s, Dealer got: %s. It's a Push!" %(player_value, dealer_value))

        else:
            print("Player got: %s, Dealer got: %s. Dealer Wins!" %(player_value, dealer_value))
            balance -= wager
    
    print("Updated Balance: %s" %balance)
    return balance