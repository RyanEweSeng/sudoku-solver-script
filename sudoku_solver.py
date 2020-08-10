def print_board(board):
    """
    Prints the sudoku board.
    :param board:
    :return:
    """
    for i in range(len(board)):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(len(board)):
            if j % 3 == 0:
                print("| ", end="")
            print(str(board[i][j]) + " ", end="")
            if j == 8:
                print("|")
    print("-------------------------")


def find_empty_pos(board):
    """
    Locates the next empty slot.
    :param board:
    :return:
    """
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return [row, col]
    return None


def is_valid(board, pos, num):
    """
    Checks if the number in the given position is valid.
    :param board: 2d array
    :param pos: array
    :param num: int
    :return: bool
    """
    # check if valid in row (row is fixed and column is varied)
    for col in range(len(board)):
        if board[pos[0]][col] == num:
            return False

    # check if valid in column (column is fixed and row is varied)
    for row in range(len(board)):
        if board[row][pos[1]] == num:
            return False

    # check if valid in sub-grid
    # first we calculate the sub-grid coordinates
    subgrid_row = (pos[0] // 3) * 3
    subgrid_col = (pos[1] // 3) * 3

    # iterate through the sub-grid
    for sub_row in range(subgrid_row, subgrid_row + 3):
        for sub_col in range(subgrid_col, subgrid_col + 3):
            if board[sub_row][sub_col] == num:
                return False

    return True


def solve(board):
    """
    Solves the board using a backtracking algorithm.
    :param board: 2D array containing the sudoku puzzle
    :return:
    """
    # First we find an empty slot
    empty_slot = find_empty_pos(board)

    # If there are no empty slots, then the sudoku puzzle is solved
    if empty_slot is None:
        return True

    # Placing the number (1-9) into the empty slot
    for num in range(1, 10):
        # Check if the number is in a valid slot
        if is_valid(board, empty_slot, num):
            board[empty_slot[0]][empty_slot[1]] = num

            # If the number is valid, we recursively call solve()
            if solve(board):
                return True

            # Once there is an incorrect number, we undo the previous step and backtrack
            board[empty_slot[0]][empty_slot[1]] = 0

    # Return false if no numbers are valid (this means that backtracking needs to be done)
    return False


# # Lvl. 1
# b0 = [[0, 0, 0, 0, 8, 0, 5, 0, 0],
#       [0, 4, 0, 9, 0, 0, 0, 6, 0],
#       [0, 0, 9, 7, 2, 6, 3, 0, 0],
#       [7, 0, 3, 2, 9, 0, 8, 4, 0],
#       [2, 0, 0, 0, 1, 0, 0, 0, 5],
#       [0, 6, 4, 0, 7, 8, 9, 0, 2],
#       [0, 0, 6, 8, 4, 7, 1, 0, 0],
#       [0, 8, 0, 0, 0, 2, 0, 9, 0],
#       [0, 0, 1, 0, 6, 0, 0, 0, 0]]
#
# # Lvl. 4
# b1 = [[4, 0, 0, 0, 1, 0, 0, 0, 6],
#       [0, 5, 9, 3, 0, 4, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 7, 0],
#       [0, 9, 0, 7, 0, 0, 6, 0, 4],
#       [0, 0, 0, 0, 8, 0, 0, 0, 0],
#       [5, 0, 4, 0, 0, 2, 0, 3, 0],
#       [0, 8, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 8, 0, 3, 9, 5, 0],
#       [3, 0, 0, 0, 9, 0, 0, 0, 2]]
#
# # Lvl. 11
# b2 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 3, 6, 0, 0, 0, 0, 0],
#       [0, 7, 0, 0, 9, 0, 2, 0, 0],
#       [0, 5, 0, 0, 0, 7, 0, 0, 0],
#       [0, 0, 0, 0, 4, 5, 7, 0, 0],
#       [0, 0, 0, 1, 0, 0, 0, 3, 0],
#       [0, 0, 1, 0, 0, 0, 0, 6, 8],
#       [0, 0, 8, 5, 0, 0, 0, 1, 0],
#       [0, 9, 0, 0, 0, 0, 4, 0, 0]]
