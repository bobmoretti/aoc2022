#%%
import numpy as np


def parse_map(fname="input.txt"):
    with open(fname) as f:
        cols = []
        for ii, line in enumerate(f):
            row = []
            for jj, char in enumerate(line.strip()):
                if char == "S":
                    start = (jj, ii)
                    char = "a"
                elif char == "E":
                    char = "z"
                    end = (jj, ii)

                row.append(ord(char) - ord("a"))
            cols.append(row)
        return start, end, np.array(cols, np.int32)


def print_state(m):
    for ii, row in enumerate(m):
        for jj, col in enumerate(row):
            if col <= 9:
                print(f"{col}", end="")
            elif col > 20000:
                print("-", end="")
            else:
                print(".", end="")
        print("")


def shortest_path(start, is_end, m: np.array):

    cur = start
    visited = set()
    costs = np.zeros(m.shape, np.int32) + np.iinfo(np.int32).max
    costs.T[start] = 0
    candidates = set()

    def get_neighbors(node_coord):
        nonlocal visited, m
        x, y = node_coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        def is_valid(x, y):
            p, q = m.T.shape
            in_bounds = x >= 0 and y >= 0 and x < p and y < q
            return (x, y) not in visited and in_bounds

        return [(x, y) for x, y in neighbors if is_valid(x, y)]

    def find_next_to_visit():
        nonlocal costs, visited, candidates

        c = np.array(list(candidates))
        candidate_costs = costs.T[c.T[0], c.T[1]]
        next = tuple(c[np.argmin(candidate_costs)])
        return next

    while True:
        visited.add(cur)
        neighbors = get_neighbors(cur)
        candidates.update(neighbors)
        for neighbor in neighbors:
            cost = m.T[cur] - m.T[neighbor]
            connected = cost <= 1
            if connected:
                new_cost = min(costs.T[neighbor], costs.T[cur] + 1)
                costs.T[neighbor] = new_cost
        cur = find_next_to_visit()
        candidates.remove(cur)
        if is_end(cur):
            print_state(costs)
            return costs.T[cur]


def part1(fname="input.txt"):
    s, e, m = parse_map(fname)

    def is_end(curr):
        nonlocal s
        return curr == s

    return shortest_path(e, is_end, m)


def part2(fname="input.txt"):
    s, e, m = parse_map(fname)
    starts = np.array(np.where(m == 0))[::-1].T

    def is_end(s):
        return m.T[s] == 0

    return shortest_path(e, is_end, m)


print(part1())
print("")
print(part2())
