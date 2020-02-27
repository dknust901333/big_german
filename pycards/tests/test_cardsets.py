from pycards.cards.cardsets import poker_cards, uno_cards
import unittest


class TestCardsets(unittest.TestCase):
    def test_set_sizes(self):
        self.assertTrue(len(poker_cards) == len(set(poker_cards)))
        self.assertTrue(len(poker_cards), 52)
        self.assertTrue(len(uno_cards), 108)


if __name__ == '__main__':
    unittest.main()
