def bubble_sort(deck):
    n = len(deck)
    for i in range(n):
        for j in range(0, n-i-1):
            if deck[j]['value'] > deck[j+1]['value']:
                deck[j], deck[j+1] = deck[j+1], deck[j]

# Your existing code
import create_deck
import random

# Creating a shuffled deck
card_deck = create_deck.card_deck
deck_to_shuffle = card_deck.copy()
random.shuffle(deck_to_shuffle)

# Sorting the shuffled deck using bubble sort
bubble_sort(deck_to_shuffle)

# Printing the sorted deck
for card in deck_to_shuffle:
    print(card)