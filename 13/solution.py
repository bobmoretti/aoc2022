#%%
from enum import Enum
from functools import cmp_to_key


def parse(fname="input.txt"):
    lines = [eval(line) for line in open(fname) if line.strip() != ""]
    return lines


class Result(Enum):
    UNKNOWN = -1
    OUT_OF_ORDER = 0
    IN_ORDER = 1


DEBUG = False


def compare(l1, l2, lvl=0):
    def indent(n, msg=""):
        if DEBUG:
            print(" " * (n * 2), end="")
            if msg != "":
                print(msg)

    indent(lvl, f"- Compare {l1} vs {l2}")
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            indent(lvl + 1, "- Left side is smaller, so inputs are in the right order")
            return Result.IN_ORDER
        elif l1 == l2:
            return Result.UNKNOWN
        else:
            indent(
                lvl + 1, "- Right side is smaller, so inputs are NOT in the right order"
            )
            return Result.OUT_OF_ORDER
    elif isinstance(l1, list) and isinstance(l2, list):
        for a, b in zip(l1, l2):
            result = compare(a, b, lvl + 1)
            if result in (Result.IN_ORDER, Result.OUT_OF_ORDER):
                return result
        if len(l1) < len(l2):
            return Result.IN_ORDER
        elif len(l1) > len(l2):
            return Result.OUT_OF_ORDER
        else:
            return Result.UNKNOWN

    else:
        if isinstance(l1, int):
            indent(
                lvl + 1, f"- Mixed types; convert left to {[l1]} and retry comparison"
            )
            return compare([l1], l2, lvl + 1)
        else:
            indent(
                lvl + 1, f"- Mixed types; convert right to {[l2]} and retry comparison"
            )
            return compare(l1, [l2], lvl + 1)


def part1(fname="input.txt"):
    lines = parse(fname)
    pairs = list(zip(lines[::2], lines[1::2]))

    return sum(
        [(ii + 1) for ii, val in enumerate(pairs) if compare(*val) == Result.IN_ORDER]
    )


def part2(fname="input.txt"):
    def cmp(l1, l2):
        return -1 if compare(l1, l2) == Result.IN_ORDER else 1

    lines = parse(fname)
    lines.append([[2]])
    lines.append([[6]])
    lines = sorted(lines, key=cmp_to_key(cmp))
    return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)


print(part1("input.txt"))
print(part2("input.txt"))

# %%
