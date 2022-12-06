#%%
# %%
class Crates:
    def __init__(self, fname="input.txt"):
        self._state = [list() for _ in range(9)]
        self._moves = []
        self._fname = fname

    def part1(self):
        self.run(self.move_lifo)

    def part2(self):
        self.run(self.move_together)

    def run(self, move_func):
        with open(self._fname) as f:
            for line in f:
                if line.strip() == "":
                    continue
                elif line.startswith("move"):
                    move = self.parse_move(line)
                    move_func(*move)
                elif line.strip().startswith("["):
                    self.parse_initial_state(line)

    def parse_initial_state(self, line):
        for index in range(9):
            c = line[index * 4 + 1]
            if c == " ":
                continue
            self._state[index].insert(0, c)

    def move(self, frm, to):
        chr = self._state[frm - 1].pop()
        self._state[to - 1].append(chr)

    def parse_move(self, line):
        return [int(x) for x in line.split()[1::2]]

    def move_lifo(self, n, frm, to):
        for _ in range(n):
            self.move(frm, to)

    def get_top(self):
        return [stack[-1] for stack in self._state]

    def move_together(self, n, frm, to):
        tmp = self._state[frm - 1][-n:]
        self._state[frm - 1] = self._state[frm - 1][:-n]
        self._state[to - 1].extend(tmp)


def part1():
    crts = Crates()
    crts.part1()
    print("".join(crts.get_top()))


def part2():
    crts = Crates()
    crts.part2()
    print("".join(crts.get_top()))


part1()
part2()
