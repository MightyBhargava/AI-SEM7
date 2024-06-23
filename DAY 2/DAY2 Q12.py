import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)

# Display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)

# Board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Font
FONT_SIZE = 60
font = pygame.font.SysFont('comicsans', FONT_SIZE)

def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20),
                                 ((col + 1) * SQUARE_SIZE - 20, (row + 1) * SQUARE_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, ((col + 1) * SQUARE_SIZE - 20, row * SQUARE_SIZE + 20),
                                 (col * SQUARE_SIZE + 20, (row + 1) * SQUARE_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 20, LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def is_winner(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True
    return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                return False
    return True

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main():
    global turn

    run = True
    clock = pygame.time.Clock()
    turn = 'X'
    game_over = False

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == ' ':
                    mark_square(clicked_row, clicked_col, turn)
                    if is_winner(turn):
                        game_over = True
                    elif is_board_full():
                        game_over = True
                    turn = 'O' if turn == 'X' else 'X'

        screen.fill(WHITE)
        draw_lines()
        draw_figures()

        if game_over:
            if is_winner('X'):
                draw_text('X wins!', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
            elif is_winner('O'):
                draw_text('O wins!', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
            elif is_board_full():
                draw_text('It\'s a draw!', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

        pygame.display.update()

if __name__ == "__main__":
    main()
