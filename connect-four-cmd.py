#! python3

import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def dropPiece():
    pass

def isValidLocation():
    pass

def getNextOpenRow():
    pass

board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        selection = int(input('Player 1, Make Your Selection (0-6):'))
    else:
        selection = int(input('Player 2, Make Your Selection (0-6):'))
    turn += 1
    turn = turn % 2