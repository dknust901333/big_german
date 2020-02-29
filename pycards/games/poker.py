from collections import Counter
from pycards.cards.cardsets import poker_cards, poker_faces


class FiveCardDraw:
    hand_scores = {
        'Straight Flush': 9,
        '4 of a Kind': 8,
        'Full House': 7,
        'Flush': 6,
        'Straight': 5,
        '3 of a Kind': 4,
        '2 Pair': 3,
        'Pair': 2,
        'High Card': 1
    }

    @staticmethod   # Static methods are defined for the class, not instances of the class
    def sort_hand(hand):
        # A sorted Poker hand should rank by frequency and value: i.e. (A, A, 2, 2, K)
        rank_sort = sorted(hand, key=lambda card: poker_faces.index(card[0]), reverse=True)
        weighted_rank_sort = sorted(rank_sort, key=lambda card: ([c[0] for c in rank_sort]).count(card[0]))
        return weighted_rank_sort

    def __init__(self, deck=poker_cards):
        self.deck = deck
        deck.shuffle()

    def score_hand(self, hand):
        score = {}
        sorted_hand = self.sort_hand(hand)
        face_counts = dict(Counter([f[0] for f in sorted_hand]))

        face_set = list(set([card[0] for card in sorted_hand]))
        suit_count = len(set([card[1] for card in sorted_hand]))

        flush_flag = (suit_count == 1)
        straight_flag = False

        if len(face_set) == 5:
            if (poker_faces.index(face_set[0]) - poker_faces.index[face_set[4]] == 4) \
                    or (poker_faces.index(face_set[1]) - poker_faces.index[face_set[4]] == 3):
                straight_flag = True

        if flush_flag and straight_flag:
            scoring_name = 'Straight Flush'
            if '2' in face_set and 'A' in face_set:
                face_set.append(face_set.pop(0))
            score['tuple_value'] = (self.hand_scores[scoring_name], poker_faces.index(face_set[0]))

        elif flush_flag:
            scoring_name = 'Flush'
            score['tuple_value'] = (self.hand_scores[scoring_name], poker_faces.index(face_set[0]))

        elif straight_flag:
            scoring_name = 'Straight'
            if '2' in face_set and 'A' in face_set:
                face_set.append(face_set.pop(0))
            score['tuple_value'] = (self.hand_scores[scoring_name], poker_faces.index(face_set[0]))

        elif face_counts.values == [4, 1]:
            scoring_name = '4 of a Kind'
            score['tuple_value'] = (
                self.hand_scores[scoring_name],
                poker_faces.index(face_set[0]),
                poker_faces.index(face_set[4])
            )

        elif face_counts.values == [3, 2]:
            scoring_name = 'Full House'
            score['tuple_value'] = (
                self.hand_scores[scoring_name],
                poker_faces.index(face_set[0]),
                poker_faces.index(face_set[3])
            )

        elif face_counts.values == [3, 1, 1]:
            scoring_name = '3 of a Kind'
            score['tuple_value'] = (
                self.hand_scores[scoring_name],
                poker_faces.index(face_set[0]),
                poker_faces.index(face_set[3]),
                poker_faces.index(face_set[4])
            )

        elif face_counts.values == [2, 2, 1]:
            scoring_name = '2 Pair'
            score['tuple_value'] = (
                self.hand_scores[scoring_name],
                poker_faces.index(face_set[0]),
                poker_faces.index(face_set[2]),
                poker_faces.index(face_set[4])
            )

        elif face_counts.values == [2, 1, 1, 1]:
            scoring_name = '1 Pair'
            score['tuple_value'] = (
                self.hand_scores[scoring_name],
                poker_faces.index(face_set[0]),
                poker_faces.index(face_set[2]),
                poker_faces.index(face_set[3]),
                poker_faces.index(face_set[4])
            )

        elif face_counts.values == [1, 1, 1, 1, 1]:
            scoring_name = 'High Card'
            score['tuple_value'] = (
                self.hand_scores[scoring_name],
                poker_faces.index(face_set[0]),
                poker_faces.index(face_set[1]),
                poker_faces.index(face_set[2]),
                poker_faces.index(face_set[3]),
                poker_faces.index(face_set[4])
            )

        score['name'] = scoring_name
        return score
