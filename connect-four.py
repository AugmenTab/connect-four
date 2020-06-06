#! python3

import numpy as np
import pygame, sys, math

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
    for c in range(COL_COUNT-3): #Check for horizontal wins
        for r in range(ROW_COUNT):
            if piece == board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                return True
    for c in range(COL_COUNT): #Check for vertical wins
        for r in range(ROW_COUNT-3):
            if piece == board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                return True
    for c in range(COL_COUNT-3): #Check for positive-slope diagonal wins
        for r in range(ROW_COUNT):
            if piece == board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                return True
    for c in range(COL_COUNT-3): #Check for negative-slope diagonal wins
        for r in range(3, ROW_COUNT):
            if piece == board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                return True

def drawBoard(board):
    for c in range(COL_COUNT):
        for r in range (ROW_COUNT):
            pygame.draw.rect(screen, (0,0,255), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (0,0,0), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

ROW_COUNT = 6
COL_COUNT = 7

board = create_board()
game_over = False
printBoard(board)
turn = 0

pygame.init()
SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE + 1
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 1)
                    if winningMove(board, 1):
                        print('PLAYER 1 WINS!')
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 2)
                    if winningMove(board, 2):
                        print('PLAYER 2 WINS!')
                        game_over = True
            printBoard(board)
            turn += 1
            turn = turn % 2