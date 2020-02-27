import random


class Deck:
    cards = []

    def __init__(self, card_list):
        self.cards = card_list

    def add_cards(self, cards_to_add):
        for c in cards_to_add:
            self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards=5):
        cards_to_deal = []
        for n in range(num_cards):
            cards_to_deal.append(self.cards.pop())
        return cards_to_deal

