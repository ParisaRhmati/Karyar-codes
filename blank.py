def initialize_board():
    board = [
        [1, 1, 2, 4, 3, 2, 1]
        [4, 4, 3, 2, 1, 3, 4]
        [2, 3, 4, 1, 2, 3, 4]
        [1, 2, 3, 4, 1, 2, 3]
        [4, 3, 2, 1, 4, 3, 2]
        [3, 2, 1, 3, 2, 1, 4]
        [2, 1, 4, 3, 2, 1, 3]
    ]
    return board


def print_board(board, points):
    print(f"Points:{points}")
    for row in board:
        print(row)


def user_choice():
    item1_row = int(input("Enter the row of the first item: ")) - 1
    item1_col = int(input("Enter the column of the first item: ")) - 1
    item2_row = int(input("Enter the row of the first item: ")) - 1
    item2_col = int(input("Enter the column of the first item: ")) - 1
    item1 = (item1_row, item1_col)
    item2 = (item2_row, item2_col)
    return item1, item2


def check_swap(board, item1, item2):
    is_swap_valid = True
    if ...:
        is_swap_valid = False
    if ...:
        is_swap_valid = False
    return is_swap_valid
