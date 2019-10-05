import unittest
from card import Card
from hand import Hand
from deck import Deck
from constants import SUITS, RANKS, Color
from utils import findWinner


class TestBlackjackFunctions(unittest.TestCase):

    def test_card(self):
        card = Card("SPADES", "ACE")
        self.assertEqual(card.getSuit(), "SPADES")
        self.assertEqual(card.getRank(), "ACE")

    def test_hand(self):
        hand = Hand()
        self.assertEqual(len(hand.cards), 0)
        self.assertEqual(hand.getCard(0), None)

        card_1 = Card("SPADES", "ACE")
        hand.addCard(card_1)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.getValue(), 11)
        self.assertEqual(hand.getCard(0), card_1)
        
        card_2 = Card("HEARTS", "ACE")
        hand.addCard(card_2)
        self.assertEqual(len(hand.cards), 2)
        self.assertEqual(hand.getValue(), 12)
        self.assertEqual(hand.getCard(1), card_2)
        self.assertTrue(hand.canSplit())

    def test_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        card = deck.dealCard()
        self.assertEqual(len(deck.cards), 51)
        self.assertFalse(card in deck.cards)

    def test_winner(self):
        # when player wins
        player = Hand()
        dealer = Hand()
        
        card_1 = Card("SPADES", "ACE")
        card_2 = Card("HEARTS", "JACK")
        card_3 = Card("CLUBS", "KING")
        card_4 = Card("DIAMONDS", "QUEEN")
        
        player.addCard(card_1)
        dealer.addCard(card_2)
        player.addCard(card_3)
        dealer.addCard(card_4)

        balance = 100
        wager = 5
        self.assertEqual(findWinner(Deck(), player, dealer, balance, wager), 105)
        
        # when it's a push
        player = Hand()
        dealer = Hand()
        card_1 = Card("SPADES", "TEN")
        
        player.addCard(card_1)
        dealer.addCard(card_2)
        player.addCard(card_3)
        dealer.addCard(card_4)

        balance = 100
        wager = 7
        self.assertEqual(findWinner(Deck(), player, dealer, balance, wager), 100)
        
        # when player loses
        player = Hand()
        dealer = Hand()
        card_1 = Card("SPADES", "TWO")
        
        player.addCard(card_1)
        dealer.addCard(card_2)
        player.addCard(card_3)
        dealer.addCard(card_4)

        balance = 100
        wager = 11
        self.assertEqual(findWinner(Deck(), player, dealer, balance, wager), 89)

if __name__ == '__main__':
    unittest.main()