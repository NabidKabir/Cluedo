characters = ["Scarlett", "Mustard", "White", "Purple"]
weapons = ["Rope", "Knife", "Revolver", "Bat"]


def make_suggestion(player, room):
    print("\nMake a suggestion:")
    suspect = input("Suspect: ")
    weapon = input("Weapon: ")

    return {
        "character": suspect,
        "weapon": weapon,
        "room": room
    }


def check_suggestion(suggestion, players, current_player):
    for player in players:
        if player == current_player:
            continue

        for card in player.cards:
            if card in suggestion.values():
                print(f"{player.name} disproves the suggestion!")
                return card

    print("No one could disprove the suggestion!")
    return None


def make_accusation():
    print("\nMake an accusation:")
    return {
        "character": input("Suspect: "),
        "weapon": input("Weapon: "),
        "room": input("Room: ")
    }


def check_accusation(accusation, solution):
    return accusation == solution