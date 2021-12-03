#!/usr/bin/env python3

from sys import argv, stderr

usage = f"""Usage: %s [<part>] <filename>
Where <part> is either 1 or 2, depending on the part of the challenge,
             default value is 1.
      <filename> is the path to the puzzle input file."""

def parse_line(line):
    # TODO
    return line

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

    lines = parse_input(file)
    count = [0 for i in range(len(lines[0]))]
    count0 = [0 for i in range(len(lines[0]))]
    for line in lines:
        for i in range(len(count)):
            count[i] += 1 if line[i] == '1' else 0
            count0[i] += 1 if line[i] == '0' else 0
    mcb = ""
    lcb = ""
    for i in range(len(count)):
        mcb += "1" if count[i] >= count0[i] else "0"
        lcb += "1" if count[i] <  count0[i] else "0"
    gamma = int("".join(list(map(str, mcb))), base=2)
    epsilon = int("".join(list(map(str, lcb))), base=2)

    if part == 1:
        print(gamma, epsilon, gamma * epsilon)
        exit(0)

    oxygen = lines.copy()
    co2    = lines.copy()
    for j in range(len(count)):
        count = [0 for i in range(len(lines[0]))]
        count0 = [0 for i in range(len(lines[0]))]
        for line in oxygen:
            for i in range(len(count)):
                count[i] += 1 if line[i] == '1' else 0
                count0[i] += 1 if line[i] == '0' else 0
        mcb = ""
        for i in range(len(count)):
            mcb += "1" if count[i] >= count0[i] else "0"
        count = [0 for i in range(len(lines[0]))]
        count0 = [0 for i in range(len(lines[0]))]
        for line in co2:
            for i in range(len(count)):
                count[i] += 1 if line[i] == '1' else 0
                count0[i] += 1 if line[i] == '0' else 0
        lcb = ""
        for i in range(len(count)):
            lcb += "1" if count[i] <  count0[i] else "0"

        oxygen = [val for val in oxygen if val[j] == mcb[j]]
        co2    = [val for val in co2    if val[j] == lcb[j]]
        print(oxygen)
        if len(oxygen) == 1:
            oxy = int(oxygen[0], base=2)
        if len(co2) == 1:
            co = int(co2[0], base=2)

    print(oxy, co, oxy * co)
