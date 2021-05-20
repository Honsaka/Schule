from typing import List


# create and show
def init_empty_grid() -> List[List[int]]:
    """
    Author:Alexander
    creates a empty grid
    :return: returns the empty grid
    """
    repeat = 0

    while repeat != 9:
        List = [[0, 0, 0, 0, 0, 0, 0, 0, 0 * 9]]


        repeat += 1

        return List


def init_candidates() -> List[List[str]]:
    """
    Author: Ayberk
    creates a list with the candidates for the cell
    :return: returns the list
    """
    repeat = 0

    while repeat != 9:
        List = [["123456789"] * 9]

        print(List)

        repeat += 1
    grid = []

    return List and grid


def print_grid(grid: List[List[int]]):
    """
    Author: Alexander
    prints the grid
    :param grid:
    """

    for i in range(9):
        grid += [[0] * 9]


    for i in range(9):
        if i == 3 or i == 6:
            print("---------------------")

        line = list()

        for j in range(9):
            if grid[i][j] != 0:
                line.append(str(grid[i][j]) + " ")
            else:
                line.append("  ")

            if j == 2 or j == 5:
                line.append("| ")

        print("".join(line))


def input_sudoku(grid: List[List[int]]):
    """
    Author:Ayberk
    you can give an input into a row
    :param grid:creates the grid
    :return: returns the grid into a newer stage
    """
    for a in range(0, 8):
        eingabe = input()
        eingabe = eingabe.split()
        for b in range(0, 8):
            if b == 0:
                grid[b][0] = eingabe[b][0]
                grid[b][1] = eingabe[b][1]
                grid[b][4] = eingabe[b][2]
                grid[b][6] = eingabe[b][3]
                grid[b][7] = eingabe[b][4]
                grid[b][8] = eingabe[b][5]
            elif b == 1:
                grid[b][0] = eingabe[b][0]
                grid[b][3] = eingabe[b][1]
                grid[b][4] = eingabe[b][2]
                grid[b][5] = eingabe[b][3]
                grid[b][6] = eingabe[b][4]
                grid[b][7] = eingabe[b][5]
                grid[b][8] = eingabe[b][6]
            elif b == 2:
                grid[b][0] = eingabe[b][0]
                grid[b][1] = eingabe[b][1]
                grid[b][2] = eingabe[b][2]
                grid[b][3] = eingabe[b][3]
                grid[b][4] = eingabe[b][4]
                grid[b][5] = eingabe[b][5]
                grid[b][8] = eingabe[b][6]
            elif b == 3:
                grid[b][0] = eingabe[b][0]
                grid[b][1] = eingabe[b][1]
                grid[b][2] = eingabe[b][2]
                grid[b][5] = eingabe[b][3]
                grid[b][6] = eingabe[b][4]
                grid[b][7] = eingabe[b][5]
            elif b == 4:
                grid[b][1] = eingabe[b][0]
                grid[b][2] = eingabe[b][1]
                grid[b][3] = eingabe[b][2]
                grid[b][4] = eingabe[b][3]
                grid[b][5] = eingabe[b][4]
                grid[b][6] = eingabe[b][5]
                grid[b][7] = eingabe[b][6]
                grid[b][8] = eingabe[b][7]
            elif b == 5:
                grid[b][1] = eingabe[b][0]
                grid[b][2] = eingabe[b][1]
                grid[b][3] = eingabe[b][2]
                grid[b][5] = eingabe[b][3]
                grid[b][6] = eingabe[b][4]
            elif b == 6:
                grid[b][0] = eingabe[b][0]
                grid[b][1] = eingabe[b][1]
                grid[b][2] = eingabe[b][2]
                grid[b][4] = eingabe[b][3]
                grid[b][6] = eingabe[b][4]
                grid[b][7] = eingabe[b][5]
                grid[b][8] = eingabe[b][6]
            elif b == 7:
                grid[b][0] = eingabe[b][0]
                grid[b][2] = eingabe[b][1]
                grid[b][4] = eingabe[b][2]
                grid[b][5] = eingabe[b][3]
                grid[b][6] = eingabe[b][4]
                grid[b][8] = eingabe[b][5]
            elif b == 8:
                grid[b][1] = eingabe[b][0]
                grid[b][3] = eingabe[b][1]
                grid[b][4] = eingabe[b][2]
                grid[b][5] = eingabe[b][3]
                grid[b][6] = eingabe[b][4]
                grid[b][7] = eingabe[b][5]

    return grid

def set_default_sudoku_grid(grid: List[List[int]]):
    """
    Author:Ayberk
    creates unchangeable numbers
    :param grid: makes the grid
    :return: returns the numbers in the grid
    """
    grid[0][2] = 1
    grid[0][3] = 2
    grid[0][5] = 7
    grid[1][1] = 6
    grid[1][2] = 2
    grid[2][6] = 9
    grid[2][7] = 4
    grid[3][3] = 9
    grid[3][4] = 8
    grid[3][8] = 3
    grid[4][0] = 5
    grid[5][0] = 7
    grid[5][4] = 3
    grid[5][7] = 2
    grid[5][8] = 1
    grid[6][3] = 1
    grid[6][5] = 2
    grid[7][1] = 7
    grid[7][3] = 8
    grid[7][6] = 4
    grid[7][7] = 1
    grid[8][0] = 3
    grid[8][2] = 4
    grid[8][8] = 8
    return grid


# Check
def is_present_in_row(grid: List[List[int]], row_index: int, digit: int) -> bool:
    """
    Author: Alexander
    Looks for the same number in the row
    :param grid: prints the grid
    :param row_index: the index of the row from your mumber
    :param digit: the number the user gives
    :return: returns the boolean
    """
    digit = 51

    row_index = 0
    a = 0
    answer = False

    for a in range(9):
        if answer == True:
            break
        else:
            if digit == grid[row_index][a]:
                answer = True
            else:
                answer = False

    print(answer)
    return answer


def is_present_in_column(grid: List[List[int]], column_index: int, digit: int) -> bool:
    """
    Author:Alexander
        Looks for the same number in the column
    :param grid: the grid you have
    :param column_index: the column of your number
    :param digit: the number the User gives
    :return: returns the bolean
    """
    r = 0
    column_index = 0
    answer2 = False

    for column_index in range(9):
        if answer2 == True:
            break
        else:
            if digit == grid[column_index][r]:
                answer2 = True
            else:
                answer2 = False

    print(answer2)
    return answer2

def is_present_in_block(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    Author:Alexander
        Looks for the same number in the block
    :param grid: the grid you have
    :param row_index: the row index of your number
    :param column_index: the column index of your number
    :param digit: the number the usere gives
    :return: returns the bolean
    """
    answer3 = False
    row_index = 0
    column_index = 0
    answer3 = False

    if column_index == 0 or column_index == 3 or column_index == 6:
        column_index = column_index
    elif column_index == 1 or column_index == 4 or column_index == 7:
        column_index = column_index - 1
    else:
        column_index = column_index - 2

    if row_index == 0 or row_index == 3 or row_index == 6:
        row_index = row_index
    elif row_index == 1 or row_index == 4 or row_index == 7:
        row_index = row_index - 1
    else:
        row_index = row_index - 2

    zahl1 = 0
    zahl2 = 0

    for zahl1 in range(3):
        for zahl2 in range(3):
            if answer3 == True:
                break
            if digit == grid[row_index][column_index]:
                answer3 = True
            else:
                answer3 = False
            column_index += 1
        row_index += 1
        column_index -= 3

    print(answer3)
    return answer3

def is_possible_in_cell(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    """
    Author:Alexander
    lookf if the number is possible
    :param grid: the grid you have
    :param row_index: the Index of your Number in the Row
    :param column_index: the Index of your Number in the Column
    :param digit: the number the user gives
    :return:
    """
    if answer == True or answer2 == True or answer3 == True:
        allanswer = True
    else:
        allanswer = False

    print(allanswer)
    return allanswer


# Solve
def remove_impossible_candidates(grid: List[List[int]], candidates: List[List[str]]):
    """
    Author: Ayberk
    removes the Impossible candidates in the cell
    :param grid: prints the grid
    :param candidates: the candidates of the cell
    :return: returns the digits that are not removed
    """
    for a in range(0, 8):
        for b in range(0, 8):
            if grid[a][b] != 0:
                List = str()
            else:
                if allanswer == True:
                    List.remove(digit)
    return List


def set_value_in_cell_by_last_candidate(grid: List[List[int]], candidates: List[List[str]]) -> bool:
    pass


def find_lonely_candidate_in_row(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidate_in_column(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidate_in_block(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidates(candidates: List[List[str]]):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
