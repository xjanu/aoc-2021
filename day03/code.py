#!/usr/bin/env python3

from sys import argv, stderr

usage = f"""Usage: %s [<part>] <filename>
Where <part> is either 1 or 2, depending on the part of the challenge,
             default value is 1.
      <filename> is the path to the puzzle input file."""

def parse_line(line):
    # TODO
    return int(line)

def parse_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    return list((map(parse_line, lines)))

if __name__ == "__main__":
    part = 1
    file = argv[-1]
    if len(argv) <= 1 or len(argv) > 3:
        print(usage, file=stderr)
    elif len(argv) == 3:
        part = int(argv[1])
        if part not in [1, 2]:
            print(usage, file=stderr)
            exit(2)

    # TODO
    print(parse_input(file))
