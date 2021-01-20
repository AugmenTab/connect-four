#! python3

import math
import numpy as np
import pygame
import sys

BLU = (0, 0, 255)
BLK = (0, 0, 0)
RED = (255, 0, 0)
YEL = (255, 255, 0)


def validate_number(number):
    if not (isinstance(number, int) and number >= 4):
        raise Exception('Your board dimensions are too small. The board must be 4x4 or larger.')


def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    for c in range(COL_COUNT - 3):  # Check for horizontal wins
        for r in range(ROW_COUNT):
            if piece == board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3]:
                return True
    for c in range(COL_COUNT):  # Check for vertical wins
        for r in range(ROW_COUNT - 3):
            if piece == board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c]:
                return True
    for c in range(COL_COUNT - 3):  # Check for positive-slope diagonal wins
        for r in range(ROW_COUNT):
            if piece == board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3]:
                return True
    for c in range(COL_COUNT - 3):  # Check for negative-slope diagonal wins
        for r in range(3, ROW_COUNT):
            if piece == board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3]:
                return True


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLU, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YEL, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()


print("Let's play Connect 4!")
ROW_COUNT = int(input('How many rows? (4+): '))
validate_number(ROW_COUNT)
COL_COUNT = int(input('How many columns? (4+): '))
validate_number(COL_COUNT)

board = create_board()
game_over = False
print_board(board)
turn = 0

pygame.init()

SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE + 1
size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font = pygame.font.SysFont('monospace', 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YEL, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        label = font.render('PLAYER 1 WINS!', 1, RED)
                        pygame.draw.rect(screen, BLK, (0, 0, width, SQUARESIZE))
                        screen.blit(label, (40, 10))
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        label = font.render('PLAYER 2 WINS!', 1, YEL)
                        pygame.draw.rect(screen, BLK, (0, 0, width, SQUARESIZE))
                        screen.blit(label, (40, 10))
                        game_over = True
            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2
            if game_over:
                pygame.time.wait(2500)
