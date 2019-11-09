from itertools import chain
actual_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def display_board(board: list) -> None:
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('-------------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('-------------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')


def make_move(board: list, player: int):
    try:
        row = int(input('What row do you want?\n'))
        column = int(input('What column do you want?\n'))
    except ValueError:

    board[row - 1][column - 1] = player


def check_win(board: list) -> bool:
    for row in board:
        minimum = min(row)
        maximum  = max(row)
        if minimum == maximum and minimum != 0:
            return True

    for column in zip(*board):
        minimum = min(column)
        maximum  = max(column)
        if minimum == maximum and minimum != 0:
            return True

    diagonals = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    for diagonal in diagonals:
        minimum = min(diagonal)
        maximum  = max(diagonal)
        if minimum == maximum and minimum != 0:
            return True






def run_game(board: list):
    turn = 0
    while 0 in chain(*board):
        if turn % 2 == 1:
            player = 2
        else:
            player = 1
        display_board(board)
        make_move(board, player)
        if check_win(board):
            print(f'player {player} won!')
            break
        turn += 1



run_game(actual_board)
