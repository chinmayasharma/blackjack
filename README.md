# Blackjack
A Python implementation of the game Blackjack. It's rules can be found here: https://www.blackjack.org/blackjack-rules/

Note - For simplicity, only Hit, Stand, Double Down, Surrender and Split have been implemented as possible actions. 

#### Author:
* Chinmaya Sharma
#### Requirements:
* Python 3

#### Usage:

##### Game:
To start the game, use the following command:
`python blackjack.py`

NOTE - If this gives any errors, try replacing `python` with `python3`

##### Tests:
To run the tests, use the following command:
`python test.py`

#### Design Choices:

The game was implemented using multiple objects, constants and utility functions. These are described in greater detail below:

##### Card Class:

Used to create card instances, and getters for SUITS and RANKS.

##### Hand Class:

Used to create card player and dealer hands. Maintains a list of cards, and keeps a running score of the hand's value.

##### Deck Class:

Used to simulate a deck of cards, and allows dealing one card at a time and shuffling the deck.

##### Utils Class:

Consists of serveral general functions that are used in the game. These include colorized print functions and a findWinner function that determines who won, and return the updated balance.

##### Constant Class:

Consists of serveral constants thatare used by multiple classes. eg - SUITS, RANKS

##### Blackjack Class (Main Game):

Consists of functions that take in user input, and runs the game based on existing rules


#### References:
* https://www.blackjackapprenticeship.com/how-to-play-blackjack/
* https://www.blackjack.org/blackjack-rules/
