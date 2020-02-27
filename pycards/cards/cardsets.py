poker_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
poker_suits = ['H', 'S', 'C', 'D']

poker_cards = [(f, s) for f in poker_faces for s in poker_suits]
euchre_cards = [(f, s) for f in poker_faces for s in poker_suits if poker_faces.index(f) > 6]

uno_faces = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw 2', 'Wild', 'Draw 4']
uno_colors = ['Red', 'Green', 'Blue', 'Yellow', 'Wild']

uno_cards = [(f, c) for f in uno_faces[1:13] for c in uno_colors[:4]] * 2 + \
    [(f, c) for f in uno_faces for c in uno_colors if f == '0' and c != 'Wild'] + \
    [(f, c) for f in uno_faces for c in uno_colors if f in ('Wild', 'Draw 4') and c == 'Wild'] * 4