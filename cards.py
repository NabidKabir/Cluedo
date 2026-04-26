import random

characters = ["Scarlett", "Mustard", "White", "Purple"]
weapons = ["Rope", "Knife", "Revolver", "Bat"]
rooms = ["Kitchen", "Library", "Hall", "Study", "Lounge"]


def setup_cards(players):
    solution = {
        "character": random.choice(characters),
        "weapon": random.choice(weapons),
        "room": random.choice(rooms)
    }

    deck = (
        [c for c in characters if c != solution["character"]] +
        [w for w in weapons if w != solution["weapon"]] +
        [r for r in rooms if r != solution["room"]]
    )

    random.shuffle(deck)

    for i, card in enumerate(deck):
        players[i % len(players)].add_card(card)

    return solution