#%%
import numpy as np


def parse(fname="input.txt"):
    rows = []
    with open(fname) as f:
        for line in f:
            line = bytes(line, "utf-8")
            rows.append(np.frombuffer(line, np.int8)[:-1] - ord("0"))
    return np.array(rows)


def is_visible_to_left(m, row, col):
    left = m[row][:col]
    me = m[row, col]
    return np.all(left < me)


def is_visible_to_right(m, row, col):
    right = m[row][col + 1 :]
    me = m[row, col]
    return np.all(right < me)


def is_visible_above(m, row, col):
    return is_visible_to_left(m.T, col, row)


def is_visible_below(m, row, col):
    return is_visible_to_right(m.T, col, row)


def part1(m):
    visible = set()
    funcs = [
        is_visible_to_left,
        is_visible_to_right,
        is_visible_above,
        is_visible_below,
    ]
    for row, col in np.ndindex(m.shape):
        if any(func(m, row, col) for func in funcs):
            visible.add((row, col))
    return len(visible)


def part2(m):
    def view_left(m, row, col):
        me = m[row, col]
        left = m[row][:col][::-1]
        blocked = np.asarray(left >= me)
        if np.any(blocked):
            return np.argmax(blocked) + 1
        else:
            return len(left)

    def view_right(m, row, col):
        me = m[row, col]
        right = m[row][col + 1 :]
        blocked = np.asarray(right >= me)
        if np.any(blocked):
            return np.argmax(blocked) + 1
        else:
            return len(right)

    def view_above(m, row, col):
        return view_left(m.T, col, row)

    def view_below(m, row, col):
        return view_right(m.T, col, row)

    funcs = [view_left, view_right, view_above, view_below]

    out = np.zeros(m.shape, np.int32)

    for row, col in np.ndindex(m.shape):
        out[row, col] = np.prod([view(m, row, col) for view in funcs])

    return np.max(out)

print(part1(parse()))
print(part2(parse()))
