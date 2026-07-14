import sys
sys.path.append("support")

from game import Game
import minimax
import alpha_beta


def choose_ai():
    print("Choose AI difficulty:")
    print("1. Minimax (slower, always optimal)")
    print("2. Alpha-Beta Pruning (faster, same optimal result)")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        return minimax
    return alpha_beta


def choose_symbol():
    choice = input("Do you want to be X or O? (X goes first): ").strip().upper()
    if choice not in ("X", "O"):
        print("Invalid choice, defaulting to X")
        return "X"
    return choice


def main():
    print("=== Tic-Tac-Toe: Human vs AI ===\n")
    ai_engine = choose_ai()
    human = choose_symbol()
    ai = "O" if human == "X" else "X"

    game = Game()
    game.print_board()

    while not game.is_game_over():
        if game.current_player == human:
            try:
                pos = int(input(f"Your move ({human}), pick 0-8: "))
            except ValueError:
                print("Enter a number between 0 and 8")
                continue

            if not game.is_valid_move(pos):
                print("That spot is taken or invalid, try again")
                continue

            game.make_move(pos, human)
        else:
            print(f"AI ({ai}) is thinking...")
            pos = ai_engine.best_move(game, ai)
            game.make_move(pos, ai)
            print(f"AI played position {pos}")

        game.print_board()

        winner = game.check_winner()
        if winner:
            if winner == human:
                print("You win!")
            else:
                print("AI wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        game.switch_player()


if __name__ == "__main__":
    main()