#! python3

ROW_COUNT = 6
COL_COUNT = 7

import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[5][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

board = create_board()
printBoard(board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1, Make Your Selection (0-6):'))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
    else:
        col = int(input('Player 2, Make Your Selection (0-6):'))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
    printBoard(board)
    turn += 1
    turn = turn % 2