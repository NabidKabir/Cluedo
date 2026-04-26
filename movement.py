import random


def roll_dice():
    return random.randint(1, 6)


def choose_room(player, rooms):
    print("Available rooms:")

    for i, room in enumerate(rooms):
        print(f"{i+1}. {room}")

    while True:
        try:
            choice = int(input("Choose room: ")) - 1
            if 0 <= choice < len(rooms):
                return rooms[choice]
        except:
            pass

        print("Invalid choice.")