
import numpy as np
from random import randint, shuffle


def print_board(board):
    """
    Prints the sudoku board.

    Args:
        board (np.ndarray): A 9x9 sudoku board represented as a numpy array.

    Returns:
        None.
    """

    boardString = ""
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += "| "

            if j == 8:
                boardString += "\n"

            if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                boardString += "- - - - - - - - - - - \n"
    print(boardString)


def find_empty(board):
    """
    Finds an empty cell in the sudoku board.

    Args:
        board (np.ndarray): A 9x9 sudoku board represented as a numpy array.

    Returns:
        tuple[int, int]|None: The position of the first empty cell found as a tuple of row and column indices, or None if no empty cell is found.
    """

    empty_indices = np.where(board == 0)
    if len(empty_indices[0]) > 0:
        return empty_indices[0][0], empty_indices[1][0]
    return None


def valid(board, pos, num):
    """
    Checks whether a number is valid in a cell of the sudoku board.

    Args:
        board (np.ndarray): A 9x9 sudoku board represented as a numpy array.
        pos (tuple[int, int]): The position of the cell to check as a tuple of row and column indices.
        num (int): The number to check.

    Returns:
        bool: True if the number is valid in the cell, False otherwise.
    """

    if num in board[pos[0], :]:
        return False

    if num in board[:, pos[1]]:
        return False

    start_i = pos[0] - pos[0] % 3
    start_j = pos[1] - pos[1] % 3
    if num in board[start_i:start_i+3, start_j:start_j+3]:
        return False
    return True


def solve(board):
    """
    Solves the sudoku board using the backtracking algorithm.

    Args:
        board (np.ndarray): A 9x9 sudoku board represented as a numpy array.

    Returns:
        bool: True if the sudoku board is solvable, False otherwise.
    """

    empty = find_empty(board)
    if not empty:
        return True

    for nums in range(1, 10):
        if valid(board, empty, nums):
            board[empty[0]][empty[1]] = nums

            if solve(board):  # recursive step
                return True
            board[empty[0]][empty[1]] = 0  # this number is wrong so we set it back to 0
    return False


def generate_board():
    """
    Generates a random sudoku board with fewer initial numbers.

    Returns:
        np.ndarray: A 9x9 sudoku board represented as a numpy array.
    """

    board = np.zeros((9, 9), dtype=int)

    # Fill the diagonal boxes
    for i in range(0, 9, 3):
        nums = list(range(1, 10))
        shuffle(nums)
        for row in range(3):
            for col in range(3):
                board[i + row][i + col] = nums.pop()

    # Fill the remaining cells with backtracking
    def fill_cells(board, row, col):
        """
        Fills the remaining cells of the sudoku board with backtracking.

        Args:
            board (np.ndarray): A 9x9 sudoku board represented as a numpy array.
            row (int): The current row index to fill.
            col (int): The current column index to fill.

        Returns:
            bool: True if the remaining cells are successfully filled, False otherwise.
        """

        if row == 9:
            return True
        if col == 9:
            return fill_cells(board, row + 1, 0)

        if board[row][col] != 0:
            return fill_cells(board, row, col + 1)

        for num in range(1, 10):
            if valid(board, (row, col), num):
                board[row][col] = num

                if fill_cells(board, row, col + 1):
                    return True

        board[row][col] = 0
        return False

    fill_cells(board, 0, 0)

    # Remove a greater number of cells to create a puzzle with fewer initial numbers
    for _ in range(randint(55, 65)):
        row, col = randint(0, 8), randint(0, 8)
        board[row][col] = 0

    return board


if __name__ == "__main__":
    board = generate_board()
    print_board(board)
    solve(board)
    print_board(board)
