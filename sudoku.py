# Your task is to write a program which:
#
# Reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# outputs Yes if the Sudoku is valid, and No otherwise.

test_data1 = {
    '1': (2, 9, 5, 7, 4, 3, 8, 6, 1),
    '2': (4, 3, 1, 8, 6, 5, 9, 2, 7),
    '3': (8, 7, 6, 1, 9, 2, 5, 4, 3),
    '4': (3, 8, 7, 4, 5, 9, 2, 1, 6),
    '5': (6, 1, 2, 3, 8, 7, 4, 9, 5),
    '6': (5, 4, 9, 2, 1, 6, 7, 3, 8),
    '7': (7, 6, 3, 5, 2, 4, 1, 8, 9),
    '8': (9, 2, 8, 6, 7, 1, 3, 5, 4),
    '9': (1, 5, 4, 9, 3, 8, 6, 7, 2)
}
test_data2 = {
    '1': (1, 9, 5, 7, 4, 3, 8, 6, 2),
    '2': (4, 3, 1, 8, 6, 5, 9, 2, 7),
    '3': (8, 7, 6, 1, 9, 2, 5, 4, 3),
    '4': (3, 8, 7, 4, 5, 9, 2, 1, 6),
    '5': (6, 1, 2, 3, 8, 7, 4, 9, 5),
    '6': (5, 4, 9, 2, 1, 6, 7, 3, 8),
    '7': (7, 6, 3, 5, 2, 4, 1, 8, 9),
    '8': (9, 2, 8, 6, 7, 1, 3, 5, 4),
    '9': (2, 5, 4, 9, 3, 8, 6, 7, 1)
}


def isSudoku(sudoku: dict):
    # Traversing values row by row:
    for v in sudoku.values():
        sum_of_digits = 0
        for i in v:
            sum_of_digits += i
        if sum_of_digits != 45:
            return False

    # Traversing values column by column
    for i in range(9):
        sum_of_digits = 0
        for k in sudoku.keys():
            sum_of_digits += sudoku[k][i]
        if sum_of_digits != 45:
            return False

    # Traversing values sub-square by sub-square
    for c in range(0, 9, 3):
        for r in range(1, 10, 3):
            sum_of_digits = 0
            for i in range(3):
                for j in range(3):
                    sum_of_digits += sudoku[str(r + i)][c + j]
            if sum_of_digits != 45:
                return False

    return True


print(isSudoku(test_data1))
print(isSudoku(test_data2))
