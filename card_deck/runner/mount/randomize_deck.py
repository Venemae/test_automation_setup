import create_deck
import random

card_deck = create_deck.card_deck

deck_to_shuffle = card_deck.copy()
<<<<<<< HEAD
=======

shuffled_deck = []

for card in deck_to_shuffle:
    
    card_side = create_deck.sides[random.randint(0, 1)]

    card_template = {}

    for key in card.keys():
        
        print(key)

        if key == "side":
            
            card_template[key] = card_side

        else:
            
            card_template[key] = card[key]

    shuffled_deck.append(card_template)

    print(f"shuffled_deck length: {len(shuffled_deck)}")
>>>>>>> e9ec508e76e99bd039de17e151e26d08b04595dc

shuffled_deck = []

for card in deck_to_shuffle:
    
    card_side = create_deck.sides[random.randint(0, 1)]
    card_template = {}
    
    for key in card.keys():
        
        print(key)
        
        if key == "side":
            
            card_template[key] = card_side
            
        else :
            
            card_template[key] = card[key]
            
    shuffled_deck.append(card_template)
    print(f"shuffeld_deck lenght: {len(shuffled_deck)}")

random.shuffle(deck_to_shuffle)

print(f"shuffled_deck length: {len(deck_to_shuffle)} and card_deck length: {len(card_deck)}")

for i in range(len(card_deck)):

    print(f"\n{50*'#'}")
    print(shuffled_deck[i])
    print(card_deck[i])
    print(50*"#", "\n")