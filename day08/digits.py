#!/usr/bin/env python3

# A lookup table of possible digits based on number of segments
lookup = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0,6,9],
    7: [8]
}

# A lookup table from digit to segment sequence
lookup2 = {
    1 : "cf",
    2 : "acdeg",
    3 : "acdfg",
    4 : "bcdf",
    5 : "abdfg",
    6 : "abdefg",
    7 : "acf",
    8 : "abcdefg",
    9 : "abcdfg",
    0 : "abcefg"
}

# Above, but reversed.
rev_lookup = {v: k for k, v in lookup2.items()}

# Return True if segments mapping is ambiguous.
def segments_uncert(segments):
    for v in segments.values():
        if len(v) != 1:
            return True
    return False

# Keep only those segments corresponding to a certain digit (val is the digit)
def keep(segment, val):
    result = list(segment)
    for i in segment:
        if i not in lookup2[val]:
            result.remove(i)
    return "".join(result)

# Generate all possible decodings of a segment sequence based on current data.
def perms(segs, segments):
    if len(segs) == 1:
        for i in segments[segs[0]]:
            yield i
        return
    for seg in segments[segs[0]]:
        for i in perms(segs[1:], segments):
            yield seg + i

# Perform a simplification on digits and segments.
def step(digits, segments):
    # simplify segments
    for k, v in digits.items():
        if len(v) == 1:
            for i in k:
                segments[i] = keep(segments[i], v[0])
    # simplify digits
    for segs, v in digits.items():
        poss = []
        for perm in perms(segs, segments):
            perm = "".join(sorted(perm))
            if perm in rev_lookup.keys():
                poss.append(rev_lookup[perm])
        digits[segs] = list(sorted(set(poss)))
    # If an arrangement of segments has an only possible number,
    # remove that number from other arrangements' possibilities.
    for k, v in digits.items():
        if len(v) == 1:
            continue
        new = v.copy()
        for i in v:
            if [i] in digits.values():
                new.remove(i)
        digits[k] = new
    # Same as above, but for the mapping.
    for k, v in segments.items():
        if len(v) == 1:
            continue
        new = list(v)
        for i in v:
            if i in segments.values():
                new.remove(i)
        segments[k] = "".join(sorted(new))


# read
with open("input", "r") as f:
    lines = f.readlines()
    s = 0
    for line in lines:
        data = line.split("|")
        digits = dict(map(lambda x: (x, lookup[len(x)]), data[0].split()))
        value = data[1].strip().split()
        segments = {
            'a': "abcdefg",
            'b': "abcdefg",
            'c': "abcdefg",
            'd': "abcdefg",
            'e': "abcdefg",
            'f': "abcdefg",
            'g': "abcdefg",
        }
        while segments_uncert(segments):
            step(digits, segments)
        num = 0
        for i in value:
            num *= 10
            num += rev_lookup["".join(sorted(map(lambda x: segments[x], i)))]
        print(num)
        s += num
    print(s)
