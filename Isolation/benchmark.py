#!/usr/bin/env python3

from game import Board, game_loop
from HumanPlayer import Human_player
from RandomPlayer import Random_player
from OnePlyPlayer import One_ply_player
from MinimaxPlayer import Minimax_player

def main():

    board_size = 8
    n_games = 100
    print_step = 10

    wins = {"left": 0, "right": 0}
    for i in range(n_games):
        board = Board(board_size)
        left_player = Minimax_player(board.left, 5)
        # left_player = One_ply_player(board.left)
        # left_player = Random_player(board.left)
        right_player = Random_player(board.right)

        winner = game_loop(board, left = left_player, right = right_player, on_turn = left_player, prints = False)
        if winner == left_player:
            wins["left"] += 1
        if winner == right_player:
            wins["right"] += 1

        if print_step > 0 and (i+1) % print_step == 0:
            print(i+1, "games played")
    
    print("left won", wins["left"], "times.")
    print("right won", wins["right"], "times.")


if __name__ == "__main__":
    main()
