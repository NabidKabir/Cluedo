from player import Player
from board import Board
from movement import roll_dice, choose_room
from suggestion import (
    make_suggestion,
    check_suggestion,
    make_accusation,
    check_accusation
)
from cards import setup_cards


def start_game():
    board = Board()
    start_pos = board.get_start_position()

    players = [
        Player("Player 1", start_pos),
        Player("Player 2", start_pos),
        Player("Player 3", start_pos)
    ]

    solution = setup_cards(players)

    current_turn = 0
    game_over = False

    while not game_over:
        player = players[current_turn]

        if not player.is_active:
            current_turn = (current_turn + 1) % len(players)
            continue

        print(f"\n--- {player.name}'s Turn ---")

        turn_done = False

        while not turn_done:
            print("\nChoose an action:")
            print("1. Move")
            print("2. View Cards")
            print("3. Make Accusation")
            print("4. End Game")

            choice = input("Enter choice: ")

            if choice == "1":
                steps = roll_dice()
                print(f"Rolled: {steps}")

                reachable_positions = board.get_reachable_positions(
                    player.position, steps
                )

                reachable_rooms = board.positions_to_rooms(reachable_positions)

                if not reachable_rooms:
                    print("No rooms reachable.")
                else:
                    chosen_room = choose_room(
                        player, list(reachable_rooms.keys())
                    )

                    player.move_to(reachable_rooms[chosen_room])
                    print(f"{player.name} moved to {chosen_room}")

                    suggestion = make_suggestion(player, chosen_room)
                    check_suggestion(suggestion, players, player)

                turn_done = True

            elif choice == "2":
                player.show_cards()

            elif choice == "3":
                accusation = make_accusation()

                if check_accusation(accusation, solution):
                    print(f"{player.name} wins! Correct accusation!")
                    game_over = True
                    return
                else:
                    print(f"{player.name} made a wrong accusation and is eliminated!")
                    player.is_active = False
                    turn_done = True

            elif choice == "4":
                print("Game ended by user.")
                game_over = True
                return

            else:
                print("Invalid choice. Try again.")

        active_players = [p for p in players if p.is_active]

        if len(active_players) == 1:
            print(f"{active_players[0].name} is the last player remaining and wins!")
            game_over = True

        current_turn = (current_turn + 1) % len(players)