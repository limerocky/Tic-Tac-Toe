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
    xs = 0
    os = 0
    
    for y in board:
        for x in y:
            if x == X:
                xs += 1
            elif x == O:
                os += 1

    return X if xs <= os else O


def actions(board):
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    newBoard = copy.deepcopy(board)
    p = player(board)

    newBoard[action[0]][action[1]] = p
    return newBoard

def winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]: #rows
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i]: #columns
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def terminal(board):
    
    if winner(board):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True

def utility(board):
    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    
    if player(board) == X:
        return maxi(board, -10, 10)[1]

    else:
        return mini(board, -10, 10)[1]

def mini(board, alpha, beta):
    if terminal(board):
        return (utility(board), None)
    v = 10
    for action in actions(board):
        val = maxi(result(board, action), alpha, beta)[0]
        if val < v:
            v = val
            a = action
        beta = min(beta, v)
        if beta <= alpha:
            break
    return (v, a)

def maxi(board, alpha, beta):
    if terminal(board):
        return (utility(board), None)
    v = -10
    for action in actions(board):
        val = mini(result(board, action), alpha, beta)[0]
        if val > v:
            v = val
            a = action
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return (v, a)

