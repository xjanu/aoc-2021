#!/usr/bin/env python3

def read_board(f):
    board = []
    for i in range(5):
        line = f.readline()
        nums = line.split()
        board.append(list(map(int, nums)))

    if len(board[4]) == 5:
        return board
    else:
        return

with open("input", "r") as f:
    ran = list(map(int, f.readline().split(',')))

    boards = []
    f.readline()
    b = read_board(f)
    while b is not None:
        f.readline()
        boards.append(b)
        b = read_board(f)

marks = [[[False] * 5 for row in b ] for b in boards]

def won(marks):
    for b in range(len(marks)):
        for row in range(5):
            if marks[b][row] == [True] * 5:
                return b
        for col in range(5):
            if [marks[b][i][col] for i in range(5)] == [True] * 5:
                return b

for i in ran:
    for b in range(len(boards)):
        for row in range(5):
            for col in range(5):
                if boards[b][row][col] == i:
                    marks[b][row][col] = True
    w = won(marks)
    while w is not None:
        print(w, boards[w], marks[w])
        s = 0
        for row in range(5):
            for col in range(5):
                if marks[w][row][col] == False:
                    s += boards[w][row][col]
        print(s, i, s*i)
        boards.pop(w)
        marks.pop(w)
        w = won(marks)
