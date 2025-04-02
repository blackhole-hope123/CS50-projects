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
    count=len(actions(board))
    if count%2==0:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                res.add((i,j))
    return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0]<0 or action[0]>2 or action[1]<0 or action[1]>2 or action not in actions(board):
        raise IndexError("The move is invalid.")
    side=player(board)
    updated_board=copy.deepcopy(board)
    updated_board[action[0]][action[1]]=side
    return updated_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board)==1:
        return X
    elif utility(board)==-1:
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board)==None:
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        row=set(board[i])
        if row==set(X):
            return 1
        elif row==set(O):
            return -1
    for j in range(3):
        col=set([board[i][j] for i in range(3)])
        if col==set(X):
            return 1
        elif col==set(O):
            return -1
    diag=set([board[i][i] for i in range(3)])
    antiDiag=set([board[i][2-i] for i in range(3)])
    if diag==set(X):
        return 1
    elif diag==set(O):
        return -1
    if antiDiag==set(X):
        return 1
    elif antiDiag==set(O):
        return -1
    if len(actions(board))==0:
        return 0
    return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    table={X:1,O:-1}
    if terminal(board):
        return None
    available_actions=list(actions(board))
    if len(available_actions)==1:
        return available_actions[0]
    scores=[0]*len(available_actions)
    for i in range(len(available_actions)):
        updated_board=result(board,available_actions[i])
        while not terminal(updated_board):
            updated_board=result(updated_board,minimax(updated_board))
        scores[i]=table[player(board)]*utility(updated_board)
    maxVal=max(scores)
    for i in range(len(scores)):
        if scores[i]==maxVal:
            return available_actions[i]
        
