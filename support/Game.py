class Game:
    def __init__(self):
        # board positions 0-8, empty string means not filled
        self.board = [" "] * 9
        self.current_player = "X"

    def print_board(self):
        b = self.board
        print()
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")
        print()

    def make_move(self, pos, player):
        if self.board[pos] == " ":
            self.board[pos] = player
            return True
        return False

    def is_valid_move(self, pos):
        return 0 <= pos <= 8 and self.board[pos] == " "

    def check_winner(self):
        # all possible winning lines
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in wins:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_draw(self):
        return " " not in self.board and self.check_winner() is None

    def is_game_over(self):
        return self.check_winner() is not None or self.is_draw()

    def get_empty_positions(self):
        return [i for i in range(9) if self.board[i] == " "]

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset(self):
        self.board = [" "] * 9
        self.current_player = "X"


def play_cli():
    game = Game()
    print("Tic-Tac-Toe - positions are numbered 0-8 left to right, top to bottom")
    game.print_board()

    while not game.is_game_over():
        try:
            pos = int(input(f"Player {game.current_player}, enter position (0-8): "))
        except ValueError:
            print("Enter a number between 0 and 8")
            continue

        if not game.is_valid_move(pos):
            print("That spot is taken or invalid, try again")
            continue

        game.make_move(pos, game.current_player)
        game.print_board()

        winner = game.check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        game.switch_player()


if __name__ == "__main__":
    play_cli()
