"""
support/minimax.py
-------------------
Core Minimax algorithm for Tic-Tac-Toe (Week 3 deliverable — Khatune Jannat).

This module expects a `board` object (from support/game.py) exposing:
    board.legal_moves()      -> list of legal move identifiers (e.g. cell indices)
    board.play(move, player) -> returns a NEW board after the move (does not mutate)
    board.winner()            -> returns 'X', 'O', or None
    board.is_full()           -> True if no moves remain
    board.other(player)       -> returns the opposing player's symbol

If game.py's actual method names differ once it's pushed, only the small
adapter section at the bottom of this file needs to change — the algorithm
itself (minimax()) does not.
"""

import math


def minimax(board, player, maximizer):
    """
    Recursively computes the game-theoretic value of `board` for `maximizer`.

    Args:
        board: current board state (must support the interface above)
        player: whose turn it is to move at this node ('X' or 'O')
        maximizer: the player we are computing the best outcome for

    Returns:
        1  if `maximizer` wins with optimal play from here
        -1 if `maximizer` loses with optimal play from here
        0  if the game is a draw with optimal play from here
    """
    winner = board.winner()
    if winner is not None:
        return 1 if winner == maximizer else -1
    if board.is_full():
        return 0

    scores = []
    for move in board.legal_moves():
        next_board = board.play(move, player)
        score = minimax(next_board, board.other(player), maximizer)
        scores.append(score)

    # The maximizer picks the best outcome for itself;
    # the opponent (minimizer) picks the worst outcome for the maximizer.
    if player == maximizer:
        return max(scores)
    else:
        return min(scores)


def best_move(board, player):
    """
    Returns the optimal move for `player` on `board` using plain Minimax.

    This is what main.py / game.py should call to get the AI's move.
    """
    best_score = -math.inf
    chosen_move = None

    for move in board.legal_moves():
        next_board = board.play(move, player)
        score = minimax(next_board, board.other(player), player)
        if score > best_score:
            best_score = score
            chosen_move = move

    return chosen_move


# ---------------------------------------------------------------------------
# Self-contained demo / test — lets you verify minimax.py works correctly
# even before support/game.py exists. Once game.py is pushed, this demo
# block can be deleted or moved into a tests/ file.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    WIN_LINES = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]

    class DemoBoard:
        """Minimal placeholder board, matching the interface minimax.py expects."""
        def __init__(self, cells="." * 9):
            self.cells = cells

        def winner(self):
            for a, b, c in WIN_LINES:
                if self.cells[a] != "." and self.cells[a] == self.cells[b] == self.cells[c]:
                    return self.cells[a]
            return None

        def is_full(self):
            return "." not in self.cells

        def legal_moves(self):
            return [i for i, c in enumerate(self.cells) if c == "."]

        def play(self, move, player):
            new_cells = self.cells[:move] + player + self.cells[move + 1:]
            return DemoBoard(new_cells)

        def other(self, player):
            return "O" if player == "X" else "X"

        def __str__(self):
            rows = [self.cells[i:i + 3] for i in (0, 3, 6)]
            return "\n".join(" | ".join(r) for r in rows)

    # Quick sanity test: AI should never lose from an empty board
    board = DemoBoard()
    print("Empty board:")
    print(board)
    move = best_move(board, "X")
    print(f"\nMinimax says X's best opening move is cell {move}")

    # Test a board where X can win immediately
    winning_board = DemoBoard("XX.......")
    move = best_move(winning_board, "X")
    print(f"\nBoard 'XX.......': Minimax picks move {move} (should be 2, to win)")
    assert move == 2, "Minimax failed to find an immediate winning move!"

    # Test a board where X must block O's win
    blocking_board = DemoBoard("OO.XX....")
    move = best_move(blocking_board, "O")
    print(f"Board 'OO.XX....': Minimax picks move {move} for O (should be 2, to win)")
    assert move == 2, "Minimax failed to find an immediate winning move for O!"

    print("\nAll sanity checks passed.")
