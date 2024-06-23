import pygame
import sys
import numpy as np
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)
BG_COLOR = (32, 178, 170)

# Display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)

# Font
FONT_SIZE = 60
font = pygame.font.SysFont('comicsans', FONT_SIZE)

# Board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Minimax algorithm functions
def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

# Function to check if there's a winner
def check_win(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True
    return False

# Function to check if the board is full (draw)
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to draw the grid lines
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

# Function to draw 'X' or 'O'
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20), ((col + 1) * SQUARE_SIZE - 20, (row + 1) * SQUARE_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, ((col + 1) * SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), (col * SQUARE_SIZE + 20, (row + 1) * SQUARE_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), int(SQUARE_SIZE / 2 - 20), LINE_WIDTH)

# Function to mark the square
def mark_square(row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

# Function to draw text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Main game loop
def main():
    global board
    run = True
    turn = 'X'
    game_over = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                if mark_square(clicked_row, clicked_col, turn):
                    if check_win(board, turn):
                        print_board(board)
                        game_over = True
                    elif is_full(board):
                        game_over = True
                    turn = 'O' if turn == 'X' else 'X'

        screen.fill(WHITE)
        draw_lines()
        draw_figures()

        if game_over:
            if check_win(board, 'X'):
                draw_text('Player X wins!', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
            elif check_win(board, 'O'):
                draw_text('Player O wins!', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
            elif is_full(board):
                draw_text('It\'s a draw!', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

        pygame.display.update()

if __name__ == "__main__":
    main()
