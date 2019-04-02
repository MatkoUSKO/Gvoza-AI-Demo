import string
import re
from itertools import product
from copy import deepcopy

def translate_tile(tile_val):
    return 'x' if tile_val else '.'

class Board_player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Board:
    def __init__(self, height, width = -1):
        self.height = height
        self.width = height if width == -1 else width
        assert self.height > 0 and self.width > 0
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        self.left = Board_player("l", self.height//2, 0)
        self.right = Board_player("r", self.height//2, self.width-1)
        self.visited[self.left.x][self.left.y] = True
        self.visited[self.right.x][self.right.y] = True

    def __str__(self):
        translated = [[translate_tile(y) for y in x] for x in self.visited]

        translated[self.left.x][self.left.y] = self.left.name
        translated[self.right.x][self.right.y] = self.right.name

        rows = [
                "{j:2} {r} {j}".format(r = ' '.join(row), j = i) 
                for i, row in enumerate(translated)
               ]

        letter_row = "   {}  ".format(' '.join(string.ascii_uppercase[:self.width]))

        rows.insert(0, letter_row)
        rows.append(letter_row)

        return "\n".join(rows)

    def is_within_board(self, pos):
        x, y = pos[0], pos[1]
        return 0 <= x < self.height and 0 <= y < self.width

    def is_valid_move(self, pos):
        x, y = pos[0], pos[1]
        return not self.visited[x][y]

    def get_board_player(self, player):
        return self.left if player.name == self.left.name else self.right

    def get_valid_moves(self, player):
        player = self.get_board_player(player)
        moves = self.get_all_moves(player)
        moves = list(filter(self.is_valid_move, moves))
        moves = list(map(lambda x: str(x[0]) + string.ascii_uppercase[x[1]], moves))
        return moves
        
    def get_all_moves(self, player):
        player = self.get_board_player(player)
        px, py = player.x, player.y
        moves = list(product([px-1, px, px+1], [py-1, py, py+1]))
        moves = list(filter(self.is_within_board, moves))
        return moves

    def apply_move(self, move, player):
        match = re.match(r"(\d+)(\w+)", move, re.I) 
        assert match
        move = match.groups()

        player = self.get_board_player(player)

        if "".join(move) not in self.get_valid_moves(player):
            return False

        x, y = int(move[0]), ord(move[1]) - ord('A')

        player.x, player.y = x, y
        self.visited[x][y] = True

        return True

    def copy(self):
        return deepcopy(self)

    def is_finished(self, on_turn):
        return len(self.get_valid_moves(on_turn)) == 0


def get_opposite(l, r, current):
    return r if current == l else l

def game_loop(board, left, right, on_turn, prints = True):
    winner = None

    while True:
        if prints:
            print(on_turn.side.name, "is on turn.")
            print(board)
        if len(board.get_valid_moves(on_turn.side)) == 0:
            winner = get_opposite(left, right, on_turn)
            break

        if not board.apply_move(on_turn.next_move(board), on_turn.side):
            print("Invalid move")
            winner = get_opposite(left, right, on_turn)
            break
        if prints:
            print("#################################")
        on_turn = get_opposite(left, right, on_turn)

    if prints:
        print("#################################")
    return winner
