import random
from game import get_opposite

class One_ply_player:
    def __init__(self, side):
        self.side = side

    def next_move(self, board):
        moves = board.get_valid_moves(self.side)
        min_move = None
        min_moves_available = 10
        
        for move in moves:
            copy_board = board.copy()
            copy_board.apply_move(move, self.side)
            opposite_player = get_opposite(board.left, board.right, self.side)
            moves_available = len(copy_board.get_valid_moves(opposite_player))

            if moves_available < min_moves_available:
                min_moves_available = moves_available
                min_move = move

        return min_move

