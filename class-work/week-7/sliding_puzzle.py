# James Ferdinand Combista 2438113

import random
import sys

def getNewPuzzle(n, original):
    board = tileLabels(n)
    if not original:
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
    n = len(board)
    empty = findEmptyTile(board)
    y, x = empty
    input_move = [' ', ' ', ' ', ' ']

    if y < n - 1:
        input_move[0] = 'W'
    if y > 0:
        input_move[2] = 'S'
    if x < n - 1:
        input_move[1] = 'A'
    if x > 0:
        input_move[3] = 'D'

    while True:
        print(f"\t\t\t  ({input_move[0]}) \nEnter WASD (or QUIT): ({input_move[1]}) ({input_move[2]}) ({input_move[3]})")
        move = input('').upper()
        if move in input_move:
            return move
        elif move.lower() == 'quit':
            sys.exit()
        else: 
            print('Invalid move')

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

def makeMove(board, move):
    empty = findEmptyTile(board)
    y, x = empty
    if move == 'W':
        board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]
    elif move == 'S':
        board[y][x], board[y - 1][x] = board[y - 1][x], board[y][x]
    elif move == 'A':
        board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
    elif move == 'D':
        board[y][x], board[y][x - 1] = board[y][x - 1], board[y][x]
    return board

def mainProgram():
    print('Welcome to the sliding puzzle game!')
    n = int(input('Enter the size of the puzzle you want to play: '))
    board = getNewPuzzle(n, False)
    moveAmount = 0
    while True:
        displayBoard(board)
        move = nextMove(board)
        board = makeMove(board, move)
        moveAmount += 1
        if board == getNewPuzzle(n, True):
            displayBoard(board)
            print('Congratulations! You won!')
            return
        if moveAmount == 31 and n == 3 or moveAmount == 80 and n == 4:
            print('Best of luck next time!')
            sys.exit()

mainProgram()