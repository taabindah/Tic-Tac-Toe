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
    if terminal(board):
        return

    count_x = board[0].count(X)+ board[1].count(X)+ board[2].count(X)
    count_o = board[0].count(O)+ board[1].count(O)+ board[2].count(O)
    if count_x > count_o:
        return O
    else:
        return X
    
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    all_actions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                all_actions.add((row,col))
    return all_actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    else:
        board_new = copy.deepcopy(board)
        board_new[action[0]][action[1]] = player(board)
        return board_new

def row_col(player,board):
    for j in range(3):
        if board[j][0] == board[j][1] == board[j][2] == player:
            return True
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    return False


def diag1(player,board):

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    return False

def diag2(player,board):
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if row_col(X,board) or diag1(X,board) or diag2(X,board):
        return X
    elif row_col(O,board) or diag1(O,board) or diag2(O,board):
        return O
    else:
        return




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X,O]:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    maxm = -math.inf
    for action in actions(board):
        maxm = max(maxm,min_value(result(board,action)))
    return maxm

def min_value(board):
    if terminal(board):
        return utility(board)
    minm = math.inf
    for action in actions(board):
        minm = min(minm, max_value(result(board,action)))
    return minm



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    for action in actions(board):
        if player(board) == X:
            if max_value(board) == min_value(result(board, action)):
                return action
        else:
            if min_value(board) == max_value(result(board, action)):
                return action





