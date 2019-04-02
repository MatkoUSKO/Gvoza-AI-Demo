import random
from game import get_opposite

def eval(board, maximising_player):
    return len(board.get_valid_moves(maximising_player))

def minimax(board, depth, max_depth, maximising_player, minimising_player, player_on_turn):
    if depth >= max_depth or board.is_finished(player_on_turn):
        return eval(board, maximising_player), None

    if maximising_player == player_on_turn:
        value = -1000000
        move = None
        moves = board.get_valid_moves(player_on_turn)

        for minimax_move in moves:
            copy_board = board.copy()

            copy_board.apply_move(minimax_move, player_on_turn)

            minimax_value, _ = minimax(copy_board, depth+1, max_depth, maximising_player, minimising_player, minimising_player)

            if minimax_value > value:
                value = minimax_value
                move = minimax_move
         
        return value, move

    else: # minimising player
        value = 1000000
        move = None
        moves = board.get_valid_moves(player_on_turn)

        for minimax_move in moves:
            copy_board = board.copy()
            copy_board.apply_move(minimax_move, player_on_turn)

            minimax_value, _ = minimax(copy_board, depth+1, max_depth, maximising_player, minimising_player, maximising_player)

            if minimax_value < value:
                value = minimax_value
                move = minimax_move

        return value, move

class Minimax_player:
    def __init__(self, side, max_depth):
        self.side = side
        self.max_depth = max_depth

    def next_move(self, board):
        opposite = get_opposite(board.left, board.right, self.side)
# def minimax(board, depth, max_depth, maximising_player, minimising_player, player_on_turn):
        value, move = minimax(board, 0, self.max_depth, self.side, opposite, self.side)

        return move

