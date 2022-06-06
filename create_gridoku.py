from random import randint, shuffle


grid = [[0 for zero in range(9)] for row in range(9)]


def gridoku_main(grid):
    """
    :param grid
    :return: filled up grid
    :c: for coordinates
    """
    box_of_integers = [i for i in range(1, 10)]
    for c in range(81):
        row = c // 9
        column = c % 9
        if grid[row][column] == 0:
            shuffle(box_of_integers)
            for char in box_of_integers:
                if char not in grid[row] and \
                        char not in (grid[0][column], grid[1][column], grid[2][column],
                                     grid[3][column], grid[4][column], grid[5][column],
                                     grid[6][column], grid[7][column], grid[8][column]):
                    if row < 3:
                        if column < 3:
                            square = [grid[c][0:3] for c in range(0, 3)]
                        elif column < 6:
                            square = [grid[c][3:6] for c in range(0, 3)]
                        else:
                            square = [grid[c][6:9] for c in range(0, 3)]
                    elif row < 6:
                        if column < 3:
                            square = [grid[c][0:3] for c in range(3, 6)]
                        elif column < 6:
                            square = [grid[c][3:6] for c in range(3, 6)]
                        else:
                            square = [grid[c][6:9] for c in range(3, 6)]
                    else:
                        if column < 3:
                            square = [grid[c][0:3] for c in range(6, 9)]
                        elif column < 6:
                            square = [grid[c][3:6] for c in range(6, 9)]
                        else:
                            square = [grid[c][6:9] for c in range(6, 9)]
                    if char not in (square[0] + square[1] + square[2]):
                        grid[row][column] = char
                        if checker(grid):
                            return grid
                        else:
                            if gridoku_main(grid):
                                return grid
            break
    grid[row][column] = 0


def checker(grid):
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                return False
    return True


def remove(grid, integer):
    for step in range(integer + 1):
        row, column = randint(0, 8), randint(0, 8)
        while grid[row][column] == 0:
            row, column = randint(0, 8), randint(0, 8)
        grid[row][column] = 0
    return grid
# remove(gridoku_main(grid), 45)