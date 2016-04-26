# -*- coding: utf-8 -*-

import os

# Brute Force Algorithm for Peg Solitaire

"""
To evaluate the bruteForce algorithm create a peg solitaire game as follows:

  >>> board = initial(5, (4,2))

This will create a 5x5 peg solitaire game (with 15 holes) and place a peg in
every hole except for (4,2) which is the hole two rows below the topmost peg.
Note that the video lecture (and slides) explains the numbering scheme for 
the pegs. For the 5x5 peg solitaire game, its numbering is as follows:

 
                    (4,4)

                (3,3)   (5,3)
     
            (2,2)   (4,2)   (6,2)

        (1,1)   (3,1)   (5,1)   (7,1)

    (0,0)   (2,0)   (4,0)   (6,0)   (8,0)


Solve this puzzle by calling following function:

  >>> solveSpecific(board)

The moves that form the solution will be printed. The final remaining peg will
be left in the middle hole (4,0) of the board.

Other solvable configurations are possible (such as starting with (4,4) as empty).
"""

def initial(n, skip):
    """Construct triangle solitaire game with n*(n+1)/2 holes each filled
    with a peg except for a specific omitted value"""

    board = {}

    for c in range(0, 2*n, 2):
        d = 0
        for r in range((2*n-c)/2):
            board[(c+d,r)] = True
            d += 1

    if skip in board:
        board[skip] = False
    return board


def solve(board, path):
    """solve board and updates path to reflect sequence of moves"""

    if len(path) == len(board)-2:
        return True

    for move in moves(board):
        path.append(move)
        makeMove(board, move)

        if solve(board, path):
            return True

        undoMove(board, move)
        del path[-1]

    return False

# note each is a delta (c, r)
directions = [ [+4, 0], [-4, 0], [+2, +2], [+2, -2], [-2, +2], [-2, -2] ]

# move is a triple [ hole, deltac, deltar ]

def moves(board):
    """Returns possible moves given board state"""

    m = []
    for hole in board:
        if board[hole]:
            for deltac, deltar in directions:
                mid = (hole[0] + deltac/2, hole[1] + deltar/2)
                end = (hole[0] + deltac,   hole[1] + deltar)
                if mid in board and board[mid] and end in board and not board[end]:
                    m.append ([hole, deltac, deltar])

    return m
    

def makeMove(board, move):
    """Execute move on a board"""

    hole, deltac, deltar = move
    mid = (hole[0] + deltac/2, hole[1] + deltar/2)
    end = (hole[0] + deltac,   hole[1] + deltar)
    board[hole] = False
    board[mid] = False
    board[end] = True

def undoMove(board, move):
    """Execute move on a board"""

    hole, deltac, deltar = move
    mid = (hole[0] + deltac/2, hole[1] + deltar/2)
    end = (hole[0] + deltac,   hole[1] + deltar)
    board[end] = False
    board[mid] = True
    board[hole] = True


def solveSpecific(board):
    """Solve board and return path of moves"""

    path = []
    solve (board, path)
    for move in path:
        print move

os.system("pause")
