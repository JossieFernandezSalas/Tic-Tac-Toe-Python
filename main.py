# Name: Jossie Esteban Fernández Salas
# Email: jossie.fernandez.salas@gmail.com
# Linkedin: linkedin.com/in/jossiefernandez

import random

board = [[0 for i in range(3)] for j in range(3)]
msg = ""


def create_board():
    n = 0
    list_tmp = []
    for i in range(3):
        for j in range(3):
            board[i][j] = n + 1
            n += 1


def display_board():
    list_tmp = []
    for i in range(3):
        for j in range(3):
            list_tmp.append(board[i][j])
    p = tuple(list_tmp)
    s = """
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    """ % p
    print(s)


# The function asks the user about their move,
# checks the input, and updates the board according to the user's decision.
def enter_move():
    while True:
        move = int(input("Enter your move: "))
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    if isinstance(board[i][j], int):
                        board[i][j] = 'O'
                        return 0
                    else:
                        print("Invalid position")


# The function draws the computer's move and updates the board.
def draw_move(first):
    if first:
        board[1][1] = "X"
    else:
        while True:
            row = (random.randrange(0, 3))
            column = (random.randrange(0, 3))
            for i in range(3):
                for j in range(3):
                    n = board[row][column]
                    if isinstance(n, int):
                        board[row][column] = 'X'
                        return 0


# The function checks if there is a tie
def is_tie(moves):
    global msg
    if moves > 8:
        msg = "It's a tie"
        return True


# The function checks horizontal winning
def horizontal_win():
    x = 0
    y = 0
    global msg
    for i in range(3):
        if x == 3:
            msg = "X WON"
            return True
        if y == 3:
            msg = "0 WON"
            return True
        else:
            x = 0
            y = 0
        for j in range(3):
            if board[i][j] == 'X': x += 1
            if board[i][j] == 'O': y += 1
    if x == 3:
        msg = "X WON"
        return True
    if y == 3:
        msg = "0 WON"
        return True


# The function checks vertical winning
def vertical_win():
    x = 0
    y = 0
    global msg
    for i in range(3):
        if x == 3:
            msg = "X WON"
            return True
        if y == 3:
            msg = "0 WON"
            return True
        else:
            x = 0
            y = 0
        for j in range(3):
            if board[j][i] == 'X': x += 1
            if board[j][i] == 'O': y += 1
    if x == 3:
        msg = "X WON"
        return True
    if y == 3:
        msg = "0 WON"
        return True


# The function checks the cross winning
def cross_win():
    x = 0
    y = 0
    global msg
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        msg = "X WON"
        return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        msg = "0 WON"
        return True


# The function checks the invert cross winning
def invert_cross_win():
    x = 0
    y = 0
    global msg
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        msg = "X WON"
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        msg = "0 WON"
        return True


# The function checks if the player won in all the possible ways
def is_win():
    if horizontal_win() or vertical_win() or cross_win() or invert_cross_win():
        return True
    else:
        return False


# The function starts the game
def tic_tac_toe():
    moves = 0
    while moves <= 8:
        if moves == 0:
            create_board()
            draw_move(True)
            display_board()
            moves += 1
        else:
            enter_move()
            moves += 1
            if is_win():
                display_board()
                print(msg)
                break
            draw_move(False)
            moves += 1
            if is_win():
                display_board()
                print(msg)
                break
            display_board()
            print(msg)


if __name__ == '__main__':
    tic_tac_toe()
