import math


def alpha_beta(board, player, maximizer, alpha, beta):
    winner = board.winner()
    if winner is not None:
        return 1 if winner == maximizer else -1
    if board.is_full():
        return 0

    if player == maximizer:
        best_score = -math.inf
        for move in board.legal_moves():
            next_board = board.play(move, player)
            score = alpha_beta(next_board, board.other(player), maximizer, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # opponent won't let this branch happen, stop looking
        return best_score
    else:
        best_score = math.inf
        for move in board.legal_moves():
            next_board = board.play(move, player)
            score = alpha_beta(next_board, board.other(player), maximizer, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def best_move(board, player):
    best_score = -math.inf
    chosen_move = None
    alpha = -math.inf
    beta = math.inf

    for move in board.legal_moves():
        next_board = board.play(move, player)
        score = alpha_beta(next_board, board.other(player), player, alpha, beta)
        if score > best_score:
            best_score = score
            chosen_move = move
        alpha = max(alpha, best_score)

    return chosen_move

