def play_clock_patience(deck):
    piles = [[] for _ in range(13)]
    current_card = deck.pop()  # Top card of 'king' pile
    exposed_count = 1

    while True:
        pile_index = int(current_card[0]) - 1  # Index of the pile (0-based)
        piles[pile_index].append(current_card)

        if len(piles[pile_index]) == 5:
            current_card = piles[pile_index].pop(0)
            exposed_count += 1
        elif len(deck) > 0:
            current_card = deck.pop()
            exposed_count += 1
        else:
            break

    return exposed_count, current_card

# Read decks
decks = []
deck = []
while True:
    line = input().strip()
    if line == "#":
        if deck:
            decks.append(deck)
        break
    elif line:
        deck.extend(line.split())
    else:
        decks.append(deck)
        deck = []

# Play and print results
for deck in decks:
    exposed_count, last_card = play_clock_patience(deck.copy())  # Use a copy of the deck
    print(f"{exposed_count:02d},{last_card}")
