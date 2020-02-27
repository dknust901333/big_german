import random
import uuid


class Deck:
    def __init__(self, card_list, deck_id=None):
        self.cards = card_list
        if not deck_id:
            self.deck_id = uuid.uuid4()
        else:
            self.deck_id = deck_id
        print('building deck with id: {}'.format(self.deck_id))

    def add_cards(self, cards_to_add):
        for c in cards_to_add:
            self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)
        print('shuffling cards in deck {}...'.format(self.deck_id))

    def deal(self, num_cards=5):
        cards_to_deal = []
        for n in range(num_cards):
            cards_to_deal.append(self.cards.pop())
        return cards_to_deal
