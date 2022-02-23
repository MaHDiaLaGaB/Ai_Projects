"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    slots = 0
    turn_x = 0
    turn_o = 0
    for row in board:
        for slot in row:
            if slot == EMPTY:
                slots += 1
            elif slot == X:
                turn_x += 1
            else:
                turn_o += 1

    if slots == 9:
        print("9")
        return X

    if turn_x < turn_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_move = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_move.add(board(i, j))
    return action_move


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board[0])):
        # check horizontal
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        # check vertical
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    cell_counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                cell_counter += 1
    if cell_counter == 0:
        return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    cell_counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                cell_counter += 1
    if cell_counter == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) is True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
