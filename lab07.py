"""Lab 07 functions"""

# Tommy May
# A01086435
# March 06

import random


def game_list():
    # creating game board
    game_board = []
    for i in range(8):
        game_board.append([])
        for j in range(8):
            game_board[i].append(random.randint(0, 99))

    # printing game board
    for i in range(8):
        for j in range(8):
            if game_board[i][j] < 10:
                print('0' + str(game_board[i][j]), end=' ')
            else:
                print(game_board[i][j], end=' ')
        print('\n')

    # input coordinates and print value
    input_correct = False
    while not input_correct:
        coordinates = input('Enter a set of coordinates to see the value located there')
        coordinates = coordinates.split()
        try:
            x_coordinate = int(coordinates[0])
            y_coordinate = int(coordinates[1])
        except IndexError:
            print('Incorrect input try again')
            continue
        except ValueError:
            print('Incorrect input try again')
            continue
        if len(coordinates) > 2:
            print('Incorrect input try again')
            input_correct = False
        elif x_coordinate < 8 and y_coordinate < 8:
            print('tha value is', game_board[y_coordinate][x_coordinate])
            input_correct = True
        else:
            print('Incorrect input try again')
            input_correct = False


def game_map():
    # create empty game dictionary
    game_dictionary = {}
    for i in range(8):
        for j in range(8):
            game_dictionary[(i, j)] = []

    # place random numbers in each spot
    for i in range(8):
        for j in range(8):
            game_dictionary[(i, j)].append(random.randint(0, 99))

    # printing game board
    for i in range(8):
        for j in range(8):
            if game_dictionary[(i, j)][0] < 10:
                print('0' + str(game_dictionary[(i, j)][0]), end=' ')
            else:
                print(game_dictionary[(i, j)][0], end=' ')
        print('\n')

    # input coordinates and print value
    input_correct = False
    while not input_correct:
        coordinates = input('Enter a set of coordinates to see the value located there')
        coordinates = coordinates.split()
        try:
            x_coordinate = int(coordinates[0])
            y_coordinate = int(coordinates[1])
        except IndexError:
            print('Incorrect input try again')
            continue
        except ValueError:
            print('Incorrect input try again')
            continue
        if len(coordinates) > 2:
            print('Incorrect input try again')
            input_correct = False
        elif x_coordinate < 8 and y_coordinate < 8:
            print('tha value is', game_dictionary[(y_coordinate, x_coordinate)][0])
            input_correct = True
        else:
            print('Incorrect input try again')
            input_correct = False


def main():
    game_list()
    game_map()


if __name__ == '__main__':
    main()
