from pycards.cards.cardsets import euchre_cards, poker_cards, uno_cards
from pycards.cards.deck import Deck


def run():
    print('In this project, decks are lists of cards')
    print('Euchre Cards:')
    print(euchre_cards)
    print
    print('Poker Cards:')
    print(poker_cards)
    print

    # Deck is a class that can be instantiated many times
    uno = Deck(uno_cards, 'UNO')
    poker = Deck(poker_cards, 'POKER')
    # uno and poker are instances of the Deck class

    # shuffle is an instance method of the deck class which shuffles the card list of the instance
    uno.shuffle()
    poker.shuffle()

    #  Deal is an instance method with a parameter, which has a default value of 5
    uno_hand = uno.deal(7)
    print('My Uno hand: {}'.format(uno_hand))

    poker_hand = poker.deal(5)
    print('My Poker hand: {}'.format(poker_hand))

    # I can do very bad things like make a deck of poker and uno cards
    mixed_deck = Deck(poker_cards + uno_cards, 'MIXED')
    mixed_deck.shuffle()
    mixed_hand = mixed_deck.deal(10)

    print('Mixing poker and uno sets is possible:')
    for card in mixed_hand:
        print(card)
