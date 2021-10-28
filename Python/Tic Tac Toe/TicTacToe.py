import numpy as np
import random

def create_board():
    b = np.zeros((3,3))
    return b

def place(board, player, position):
    i = position[0]
    j = position[1]
    if board[i][j] == 0:
        board[i][j] = player

def possibilities(board):
    x = np.where(board == 0)
    a = []
    for i in range(len(x[0])):
        a.append((x[0][i], x[1][i]))   
    return a

# random.seed(1)

def random_place(board, player):
    selection = possibilities(board)
    x = random.choice(selection)
    board[x[0]][x[1]] = player
    return board

def row_win(board, player):
    for i in range(3):
        k = set(board[i])
        if len(k) == 1 and player in k:
            return True
    return False

def col_win(board, player):
    for i in range(3):
        k = set(board[:,i])
        if len(k) == 1 and player in k:
            return True
    return False 

def diag_win(board, player):
    d1 = []
    d2 = []
    for i in range(3):
        for j in range(3):
            if i == j:
                d1.append(board[i][j])
            if i + j == 2:
                d2.append(board[i][j])
    d1 = set(d1)
    d2 = set(d2)
    if len(d1) == 1 and player in d1:
        return True
    elif len(d2) == 1 and player in d2:
        return True
    else:
        return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board = create_board()
    while True:
        for player in [1,2]:
            board = random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result 

# results = [play_game() for i in range(1000)]
# print(results.count(1))

# random.seed(1)

def play_strategic_game(player, player2):
    board = create_board()
    board[1,1] = player
    while True:
        for player in [player2, player]:
            board = random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result   

# results2 = [play_strategic_game(1) for i in range(1000)]
# print(results2.count(1))
