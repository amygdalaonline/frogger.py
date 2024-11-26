"""
File:    frogger.py
Author:  Kayla Maglalang
Date:    11/16/2024
Section: 20-LEC (1321), 24-DIS (1325)
E-mail:  kmaglal1@umbc.edu
Description: frogger game in python
"""

"""
    *** NOTE: Extension granted by Professor Shivadekar via email
    *** New due date: Monday, November 26th, 2024 by 11:59:59 PM
"""

import os
root, directories, files = next(os.walk('.'))

FROG = '\U0001F438'

def select_game_file():
    """
    a function to choose which file the player wants to use
    :return: the game file the user wants to play
    """

    print("[1]\tgame1.frog\n[2]\tgame2.frog\n[3]\tgame3.frog\n[4]\tI want " + \
          "to use a different file not listed here")
    selection = input("Enter an option or filename: ")
    selection = selection.lower().strip()

    while ((selection != "1") and (selection != "2") and (selection != "3")
            and (selection != "4") and (selection != "game1.frog")
            and (selection != "game2.frog") and (selection != "game3.frog")):
        print("[1]\tgame1.frog\n[2]\tgame2.frog\n[3]\tgame3.frog")
        selection = input("Enter an option or filename: ")
        selection = selection.lower().strip()

    if selection == "4":
        print("Enter the number of the file you want to use")
        print("For example, if you want to use game7.frog, enter \"7\" " + \
              "not \"game7.frog\"")
        selection = input("Enter number: ")

    return selection


def file_reader(file):
    """
    a function to get the board portion of the file
    :param file: file chosen by user
    :return: 2d array of the board
    """

    board = [[]]
    for x in range(get_col_nums(file)):
        board[0].append("_")

    with open(file) as f:
        file_lines = len(f.readlines())
        lines_of_board = file_lines - 2
        get_board = read_last_n_lines(file, lines_of_board)

        for line in get_board:
            row = (list(line))

            if "\n" in row:
                row.remove("\n")

            board.append(row)

    board.append([])

    for x in range(get_col_nums(file)):
        board[len(board) - 1].append("_")

    return board


def read_last_n_lines(file, n):
    """
    a function to
    :param file: file chosen by user
    :param n: the number of lines to read
    :return: content from line n
    """

    with open(file) as f:
        lines = f.readlines()
        return lines[-n:]


def get_row_nums(file):
    """
    a function to get the number of rows
    :param file: file chosen by user
    :return: int representing number of rows
    """

    with open(file) as f:
        line = f.readline().strip()

    values = [int(x) for x in line.split()]

    return values[0]


def get_col_nums(file):
    """
    a function to get the number of columns
    :param file: file chosen by user
    :return: int representing number of columns
    """

    with open(file) as f:
        line = f.readline().strip()

    values = [int(x) for x in line.split()]

    return values[1]


def get_max_jumps(file):
    """
    a function to get the number of maximum jumps per round
    :param file: file chosen by user
    :return: int representing number of maximum jumps per round
    """

    with open(file) as f:
        line = f.readline().strip()

    values = [int(x) for x in line.split()]

    return values[2]


def get_frog_starting_position(file):
    """
    a function to get the starting x-coordinate of the frog
    :param file: file chosen by user
    :return: int representing the frog's starting x-coordinate
    """

    num_of_cols = get_col_nums(file)

    return num_of_cols // 2


def get_car_speeds(file):
    """
    a function to get the speeds of the cars
    :param file: file chosen by user
    :return: list of speeds of the cars
    """

    with open(file) as f:
        next(f)
        line = f.readline().strip()

    values = [int(x) for x in line.split()]

    return values


def drive_cars(file, current_board):
    """
    a function to rotate/drive the cars
    :param file: file chosen by user
    :param current_board: 2d array of the game board
    :return: 2d array with the cars rotated/driven
    """

    speeds = get_car_speeds(file)
    rows = get_row_nums(file)

    for row in range(rows):
        speed = speeds[row]

        for i in range(speed):
            current_board[row + 1].insert(0, current_board[row + 1].pop())

    return current_board


def move_frog(frog_position_x, frog_position_y, grid):
    """
    a function to move the frog
    :param frog_position_x: int representing the x-coordinate of the frog
    :param frog_position_y: int representing the y-coordinate of the frog
    :param grid: 2d array of the game board
    :return: 2d array with the frog in a new position
    """

    grid[frog_position_y][frog_position_x] = FROG

    return grid


def crash_checker(frog_position_x, frog_position_y, grid):
    """
    a function to detect crashes between the frog and the cars
    :param frog_position_x: int representing the x-coordinate of the frog
    :param frog_position_y: int representing the y-coordinate of the frog
    :param grid: 2d array of the game board
    :return: boolean, False if no crash, True if crash
    """

    crash = False

    if grid[frog_position_y][frog_position_x] == "X":
        crash = True

    return crash


def frogger_game(file):
    """
    the main game loop
    :param file: file chosen by the player
    :return: none
    """

    col_nums = 0

    if file == "1" or file == "game1.frog":
        chosen_file = "game1.frog"
        col_nums = "1 2 3 4 5 6 7 8 9 10111213141516"

    elif file == "2" or file == "game2.frog":
        chosen_file = "game2.frog"
        col_nums = "1 2 3 4 5 6 7 8 9 10111213141516171819"

    elif file == "3" or file == "game3.frog":
        chosen_file = "game3.frog"
        col_nums = "1 2 3"

    else:
        choice = ["game", file, ".frog"]
        chosen_file = "".join(choice)

    cars = file_reader(chosen_file)
    board = file_reader(chosen_file)
    max_jumps = get_max_jumps(chosen_file)
    grid_rows = get_row_nums(chosen_file)
    grid_cols = get_col_nums(chosen_file)
    frog_x = get_frog_starting_position(chosen_file)
    frog_y = 0
    board[frog_y][frog_x] = FROG

    print()
    print(f"Maximum jumps: {max_jumps}")
    print()
    print(col_nums)
    print("\n".join(" ".join(str(el) for el in row) for row in board))
    print()

    crash = crash_checker(frog_x, frog_y, board)

    while frog_y < (get_row_nums(chosen_file) + 1) and crash == False:
        move = input("WASDJ >> ")

        if not move:
            cars = drive_cars(chosen_file, cars)
            board = [row[:] for row in cars]
            move_frog(frog_x, frog_y, board)
            crash = crash_checker(frog_x, frog_y, cars)

        if move == "s":
            cars = drive_cars(chosen_file, cars)
            board = [row[:] for row in cars]
            frog_y += 1
            move_frog(frog_x, frog_y, board)
            crash = crash_checker(frog_x, frog_y, cars)

        elif move == "a":
            cars = drive_cars(chosen_file, cars)
            board = [row[:] for row in cars]
            frog_x -= 1
            move_frog(frog_x, frog_y, board)
            crash = crash_checker(frog_x, frog_y, cars)

        elif move == "d":
            cars = drive_cars(chosen_file, cars)
            board = [row[:] for row in cars]
            frog_x += 1
            move_frog(frog_x, frog_y, board)
            crash = crash_checker(frog_x, frog_y, cars)

        elif move == "w":
            cars = drive_cars(chosen_file, cars)
            board = [row[:] for row in cars]
            frog_y -= 1
            move_frog(frog_x, frog_y, board)
            crash = crash_checker(frog_x, frog_y, cars)

        elif move.startswith("j"):
            # first value is "j," second is the row, third is the column
            jump = move.split()
            row = int(jump[1])
            col = int(jump[2]) - 1

            if max_jumps == 0:
                print("Froggy is out of jumps!")

            else:
                row_diff = abs(row - frog_y)

                if ((row_diff == 1) and (row < grid_rows) and (row >= 0) and
                     (col >= 0) and (col < grid_cols)):
                    cars = drive_cars(chosen_file, cars)
                    board = [row[:] for row in cars]
                    frog_x = col
                    frog_y = row
                    move_frog(frog_x, frog_y, board)
                    crash = crash_checker(frog_x, frog_y, cars)
                    max_jumps -= 1



        print()
        print(col_nums)
        print("\n".join(" ".join(str(el) for el in row) for row in board))
        print()

    if crash:
        print("Oh no Froggy crashed... :(")

    else:
        print("Froggy is safe! :)")


if __name__ == '__main__':
   selected_game_file = select_game_file()
   frogger_game(selected_game_file)
