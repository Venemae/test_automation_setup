import create_deck
import random

card_deck = create_deck.card_deck

shuffled_deck = card_deck.copy()

random.shuffle(shuffled_deck)

print(f"shuffled_deck length: {len(shuffled_deck)} and card_deck length: {len(card_deck)}")

for i in range(len(card_deck)):

    print(f"\n{50*'#'}")
    print(shuffled_deck[i])
    print(card_deck[i])
    print(50*"#", "\n")