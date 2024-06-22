import matplotlib.pyplot as plt
import numpy as np


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens_util(board, col):
    # If all queens are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 'Q'

            # Recur to place rest of the queens
            if solve_nqueens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen
            board[i][col] = '.'

    # If the queen cannot be placed in any row in this column col then return false
    return False


def solve_nqueens():
    N = 8  # For 8x8 board
    board = [['.' for _ in range(N)] for _ in range(N)]

    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    visualize_board(board)
    return True


def visualize_board(board):
    N = len(board)
    board_visual = np.zeros((N, N, 3), dtype=float)

    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                board_visual[i, j] = [1.0, 1.0, 1.0]  # White color
            else:
                board_visual[i, j] = [0.0, 0.0, 0.0]  # Black color

            if board[i][j] == 'Q':
                plt.text(j, i, 'Q', fontsize=25, ha='center', va='center', color='red')

    plt.imshow(board_visual)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.show()


# Run the solver
solve_nqueens()
