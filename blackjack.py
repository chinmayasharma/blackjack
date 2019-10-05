'''
Developed as part of KPCB Engineering Fellowship 2019.
Auttor - Chinmaya Sharma
'''
from card import Card
from hand import Hand
from deck import Deck
from constants import SUITS, RANKS, Color
import utils


balance = 100.0

def engine(player, dealer, deck, wager):
    """ Returns void

    Handles all possible recurring actions in the game
    """

    global balance
    while player.getValue() < 21:
        choice = input("Hit - H, Stand - S, Double Down - D, Surrender - SU: ").upper()
        # hit
        if choice == "H":
            player.addCard(deck.dealCard())
            print("Player's hand: " + utils.printColored(player, Color.YELLOW))
        # stand
        elif choice == "S": 
            break
        # double down
        elif choice == "D": 
            if balance >= wager * 2:
                player.addCard(deck.dealCard())
                print("Player's hand: " + utils.printColored(player, Color.YELLOW))
                wager *= 2
                print("Updated Wager: %d" %wager)
            else:
                print("Inadequate balance. Double Down unsuccessful :(")
        # surrender
        elif choice == "SU": 
            wager *= 0.5
            print("Updated Wager: %f" %wager)
            break

        else:
            print("!! Invalid Choice !! Please choose one of (H, S, D, SU)")

    balance = utils.findWinner(deck, player, dealer, balance, wager)


def deal():
    """ Returns void

    Deals cards, and checks for splitting
    """

    while True:
        try:
            wager = int(input("Place wager: "))
            if 1 <= wager <= balance:
                break
            else:
                print("!! Invalid Choice!! Please pick a number between 1 and %d" %balance)
        except ValueError:
            print("!! Invalid Choice!! Please pick a number between 1 and %d" %balance)

    deck = Deck()
    player = Hand()
    dealer = Hand()
    
    # deal two cards each for player and dealer
    for i in range(2):
        player.addCard(deck.dealCard())
        dealer.addCard(deck.dealCard())

    card_1 = player.getCard(0)
    card_2 = player.getCard(1)
    upcard = dealer.getCard(0)
    utils.printStatus(upcard, player)
    
    # check for splitting
    if player.canSplit(): 
        while True:
            choice = input("Would you like to Split (Y / N): ").upper()
            if choice == "Y":
                if  balance < wager * 2:
                    print("Inadequate balance :(")
                else:
                    print("Splitting into two hands. \nHand #1")
                    player = Hand()
                    player.addCard(card_1)
                    player.addCard(deck.dealCard())
                    utils.printStatus(upcard, player)
                    engine(player, dealer, deck, wager)

                    # checks for adequate balance
                    if balance >= wager:
                        print("Hand #2")
                        player = Hand()
                        dealer = Hand()
                        player.addCard(card_2)
                        player.addCard(deck.dealCard())

                        for i in range(2):
                            dealer.addCard(deck.dealCard())

                        upcard = dealer.getCard(0)
                        utils.printStatus(upcard, player)
                        engine(player, dealer, deck, wager)
                    else:
                        print("Inadequate balance. Unable to play Hand #2 :(")
                    break
            elif choice == "N":
                engine(player, dealer, deck, wager)
                break
            else:
                print("!! Invalid Choice !! Please choose one of (Y / N)")
    else:
        engine(player, dealer, deck, wager)
    

def startGame():
    """ Returns void

    Main function, serves as entry point into game
    """
    print("Welcome to a game of Blackjack, A game where everybody is trying their luck. You're try to make money, while I try to become a KPCB Fellow")
    global balance

    while balance > 0:
        deal()
        choice = input("Exit - E, Any other key to continue: ").upper()
        if choice == "E":
            break
    if balance <= 0:
        print("Whoops... Out of balance.") 


if __name__ == "__main__":
    startGame()
