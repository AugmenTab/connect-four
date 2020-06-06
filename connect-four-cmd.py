#! python3

ROW_COUNT = 6
COL_COUNT = 7

import numpy as np

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[ROW_COUNT-1][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def winningMove(board, piece):
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if piece == board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                return True
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if piece == board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                return True

board = create_board()
game_over = False
printBoard(board)
turn = 0

while not game_over:
    if turn == 0:
        col = int(input('Player 1, Make Your Selection (0-6):'))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
            if winningMove(board, 1):
                print('PLAYER 1 WINS!')
                game_over = True
    else:
        col = int(input('Player 2, Make Your Selection (0-6):'))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
            if winningMove(board, 2):
                print('PLAYER 2 WINS!')
                game_over = True
    printBoard(board)
    turn += 1
    turn = turn % 2