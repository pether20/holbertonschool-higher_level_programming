#!/usr/bin/python3
"""N Queens problem"""


def isSafe(bo, row, col):
    """Checks if position is safe from attack.
    Args:
        bo: The board state.
        row: The row to check.
        col: The colum to check.
    """
    for c in range(col):
        if bo[c] is row or abs(bo[c] - row) is abs(c - col):
            return False
    return True


def checkBoard(bo, col):
    """Checks the board state column by column using backtracking.
    Args:
        bo: The board state.
        col: The current colum to check.
    """
    nm = len(bo)
    if col is nm:
        print(str([[c, bo[c]] for c in range(nm)]))
        return

    for row in range(nm):
        if isSafe(bo, row, col):
            bo[col] = row
            checkBoard(bo, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = 0
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(n)]
    checkBoard(board, 0)
