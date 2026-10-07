# Problem: N-Queens using Backtracking and Consistency Checking


def is_safe(board, row, col, n):
    """
    Check whether placing a queen at (row, col) is safe.
    """

    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(board, row, n):
    """
    Backtracking function to find a solution.
    """

    # Base condition: all queens are placed
    if row == n:
        return True

    # Try every column in the current row
    for col in range(n):

        # Consistency checking
        if is_safe(board, row, col, n):

            # Place queen
            board[row] = col

            # Recursively solve the next row
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board, n):
    """
    Display the chessboard.
    """

    for row in range(n):
        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()




n = int(input("Enter the value of N: "))

# Initially no queen is placed
board = [-1] * n

# Solve the problem
if solve_n_queens(board, 0, n):
    print("\nSolution found:")
    print_board(board, n)
else:
    print("\nNo solution exists.")

