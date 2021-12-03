#!/usr/bin/env python3

from sys import argv, stderr

usage = f"""Usage: %s [<part>] <filename>
Where <part> is either 1 or 2, depending on the part of the challenge,
             default value is 1.
      <filename> is the path to the puzzle input file."""

# Return a list of lines
def parse_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    return lines

# Return the most- and least-common bits in each column of input
def count_bits(lines):
    if len(lines) == 0:
        return "", ""

    count1 = [0 for i in range(len(lines[0]))]
    count0 = count.copy()

    for line in lines:
        for i in range(len(count)):
            count1[i] += 1 if line[i] == '1' else 0
            count0[i] += 1 if line[i] == '0' else 0

    mcb = ""
    lcb = ""
    for i in range(len(count1)):
        mcb += "1" if count1[i] >= count0[i] else "0"
        lcb += "1" if count1[i] <  count0[i] else "0"

    return mcb, lcb

# First part
def part_1(lines):
    mcb, lcb = count_bits(lines)
    gamma = int(mcb, base=2)
    epsilon = int(lcb, base=2)
    print(gamma * epsilon)

# Second part
def part_2(lines):
    oxy_lines = lines.copy()
    co2_lines = lines.copy()

    for bit in range(len(lines[0])):
        mcb, _ = count_bits(oxy_lines)
        _, lcb = count_bits(co2_lines)

        oxy_lines = [val for val in oxy_lines if val[bit] == mcb[bit]]
        co2_lines    = [val for val in co2_lines    if val[bit] == lcb[bit]]

        if len(oxy_lines) == 1:
            oxy = int(oxy_lines[0], base=2)
        if len(co2_lines) == 1:
            co2 = int(co2_lines[0], base=2)

    print(oxy * co2)

if __name__ == "__main__":
    # Parse arguments
    part = 1
    file = argv[-1]
    if len(argv) <= 1 or len(argv) > 3:
        print(usage, file=stderr)
    elif len(argv) == 3:
        part = int(argv[1])

    # Read file
    lines = parse_input(file)

    # solution.run()
    if part == 1:
        part_1(lines)
    elif part == 2:
        part_2(lines)
    else:
        print(usage, file=stderr)
        exit(2)
