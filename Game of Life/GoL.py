import numpy as np
from typing import Tuple, List
import time
from os import system

def init():
    # board = np.array([
    #     [0, 1, 0],
    #     [0, 1, 0],
    #     [0, 1, 0]
    # ])
    board = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    # board = np.array([
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ])
    mainLoop(board)

def mainLoop(board: np.ndarray):
    while True:
        system('cls')
        print('\n'.join(''.join([' ', 'X'][a] for a in line) for line in board))
        boardNew = board.copy()
        for x in range(len(board)):
            for y in range(len(board[0])):
                boardNew[x][y] = GoL((x, y), board)
        board = boardNew.copy()
        time.sleep(0.5)

def GoL(square: Tuple[int, int], board: np.ndarray) -> None:
    x, y = square #type int, int
    value = board[x][y] # type: int
    n = neighbours(square, board) # type: int
    if value:
        if n in range(0, 2) or n in range(4, 9):
            return 0
    else:
        if n == 3:
            return 1
    return value

def neighbours(square: Tuple[int, int], board: np.ndarray) -> None:
    x, y = square # type: int, int
    x_max = len(board) # type: int
    y_max = len(board[0]) # type: int
    x_rel, y_rel = -1, -1 # type: int, int
    n = 0
    while True:
        x_abs = x + x_rel
        y_abs = y + y_rel
        if x_abs in range(0, x_max) and y_abs in range(0, y_max) and (x_rel or y_rel):
            if board[x_abs][y_abs]:
                n += 1
        x_rel += 1
        if x_rel == 2:
            if y_rel == 1:
                break
            y_rel += 1
            x_rel = -1
    return n

def change(squares: List[Tuple[int, int]], board: np.ndarray):
    for square in squares:
        x, y = square
        board[x][y] = int(not board[x][y])

if __name__ == '__main__':
    init()