#!/usr/bin/env python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str((self.x, self.y))
    __repr__ = __str__

class Line:
    def __init__(self, a, b):
        self.a = a if a.x <= b.x else b
        self.b = b if a.x <= b.x else a
    def __str__(self):
        return str([self.a, self.b])
    __repr__ = __str__

    def get_xs(self):
        s = sorted([self.a.x, self.b.x])
        return s[0], s[1]

    def get_ys(self):
        s = sorted([self.a.y, self.b.y])
        return s[0], s[1]

def get_input(name):
    with open(name, "r") as f:
        lines = []
        line = f.readline()
        while line:
            a, b = line.split(" -> ")
            a, b = a.split(","), b.split(",")
            lines.append(Line(Point(int(a[0]), int(a[1])), Point(int(b[0]), int(b[1]))))
            line = f.readline()
    return lines

def draw_line_x(line, sea):
    for x in range(line.get_xs()[0], line.get_xs()[1]+1):
        sea[line.a.y][x] += 1

def draw_line_y(line, sea):
    for y in range(line.get_ys()[0], line.get_ys()[1]+1):
        sea[y][line.a.x] += 1

def draw_line_dia(line, sea):
    for d in range(abs(line.a.x - line.b.x)+1):
        if line.a.y > line.b.y:
            sea[line.a.y - d][line.a.x + d] += 1
        else:
            sea[line.a.y + d][line.a.x + d] += 1


def print_sea(sea):
    for row in sea:
        for col in row:
            print(int(col) if col != 0 else ".", end="")
        print()

SIZE = 1000

if __name__ == "__main__":
    lines = get_input("input")
    sea = [[0 for x in range(SIZE)] for y in range(SIZE)]
    for line in lines:
        if line.a.x == line.b.x:
            draw_line_y(line, sea)
        elif line.a.y == line.b.y:
            draw_line_x(line, sea)
        else:
            draw_line_dia(line, sea)
        #print_sea(sea)
    s = 0
    for row in sea:
        for col in row:
            if col >= 2:
                s += 1
    print_sea(sea)
    print(s)
