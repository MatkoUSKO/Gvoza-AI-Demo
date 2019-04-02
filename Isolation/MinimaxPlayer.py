import random
from game import get_opposite

def minimax(board, depth, max_depth, maximising_player, minimising_player, player_on_turn):
    pass

class Minimax_player:
    def __init__(self, side, max_depth):
        self.side = side
        self.max_depth = max_depth

    def next_move(self, board):
        opposite = get_opposite(board.left, board.right, self.side)
        value, move = minimax(board, 0, self.max_depth, self.side, opposite, self.side)

        return move

