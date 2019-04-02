#!/usr/bin/env python3

from game import Board, game_loop
from HumanPlayer import Human_player
from RandomPlayer import Random_player
from OnePlyPlayer import One_ply_player
from MinimaxPlayer import Minimax_player

def main():
    board = Board(5)

    left_player = Minimax_player(board.left, 6)
    # left_player = One_ply_player(board.left)
    # left_player = Random_player(board.left)
    right_player = Random_player(board.right)

    winner = game_loop(board, left = left_player, right = right_player, on_turn = left_player)


    print("The winner is", winner.side.name)
    print(board)


if __name__ == "__main__":
    main()
