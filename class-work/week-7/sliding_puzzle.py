# James Ferdinand Combista 2438113

import random
import sys

def getNewPuzzle(n):
    board = tileLabels(n)
    random.shuffle(board)
    fullBoard = []
    for i in range(0, len(board), n):
        fullBoard.append(board[i:i + n])
    return fullBoard

def tileLabels(n):
    boardtiles = []
    for i in range(1, (n**2)):
        if i < 10:
            boardtiles.append(str(i) + ' ')
        else:
            boardtiles.append(str(i))
    boardtiles.append('  ')
    return boardtiles

def findEmptyTile(board):
    for i in range(len(board)):
        for j, number in enumerate(board[i]):
            if number == '  ':
                emptySpaces = (i, j)
    return emptySpaces

def nextMove(board): 
    # if board ==
    
    print("\t\t\t  (W)\nEnter WASD (or QUIT): ( ) (S) (D)")

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

board2 = getNewPuzzle(3)
displayBoard(board2)
findEmptyTile(board2)
nextMove(board2)