import random

class Random_player:
    def __init__(self, side):
        self.side = side

    def next_move(self, board):
        moves = board.get_valid_moves(self.side)
        move = random.choice(moves)
        return move



