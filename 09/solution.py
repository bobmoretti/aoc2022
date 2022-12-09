#%%
class Position:
    def __init__(self, a=0, b=0):
        self.pos = (a, b)

    def __add__(self, rhs):
        a, b = self.pos
        c, d = rhs
        return Position(a + c, b + d)

    def __sub__(self, rhs):
        a, b = self.pos
        c, d = rhs
        return Position(a - c, b - d)

    def __getitem__(self, item):
        return self.pos[item]

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self):
        return repr(self.pos)


move_delta = {
    "U": Position(0, 1),
    "D": Position(0, -1),
    "L": Position(-1, 0),
    "R": Position(1, 0),
}


def manhattan(x: Position, y: Position):
    dx, dy = (x - y).pos
    dx = abs(dx)
    dy = abs(dy)
    return max(dx, dy)


def visualize(snake: list, visited):
    n = max(30, max((max(x, y) for x, y in visited)))
    for y in range(n, -n, -1):
        for x in range(-n, n):
            p = Position(x, y)
            if p == snake[0]:
                print("H", end="")
            elif p in snake:
                print(str(snake.index(p)), end="")
            elif p.pos == (0, 0):
                print("s", end="")
            elif p in visited:
                print("#", end="")
            else:
                print(".", end="")
        print("\n", end="")


def run_input(moves, snakelen=2):

    rope = [Position() for _ in range(snakelen)]
    visited = set((rope[-1],))

    def single_move(head_delta: Position):
        nonlocal rope
        rope[0] += head_delta
        for idx in range(len(rope) - 1):
            head = rope[idx]
            tail = rope[idx + 1]
            if manhattan(head, tail) <= 1:
                return

            dx, dy = (head - tail).pos
            if abs(dx) == 2:
                dx = dx // 2
            if abs(dy) == 2:
                dy = dy // 2

            inc = Position(dx, dy)

            rope[idx + 1] += inc
        visited.add(rope[-1])

    def handle_move(move):
        head_delta = move_delta[move[0]]
        n = int(move[1:])
        for _ in range(n):
            single_move(head_delta)

    for move in moves:
        handle_move(move)

    return visited


def part1(fname="input.txt"):
    print(len(run_input(open(fname), 2)))


def part2(fname="input.txt"):
    print(len(run_input(open(fname), 10)))


part1()
part2()
