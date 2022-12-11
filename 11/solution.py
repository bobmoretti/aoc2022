#%%

from dataclasses import dataclass
from typing import Callable
from operator import add, mul
import math

@dataclass
class Monkey(object):
    items: list[int]
    operands: list[int]
    op: Callable
    test: int
    targets: tuple[int, int]

    def do_op(self, x: int):
        fix_operands = lambda y: x if y < 0 else y
        return self.op(*(fix_operands(operand) for operand in self.operands))


def parse_monkey_str(s):
    lines = s.split("\n")
    items = [int(x) for x in lines[1].split(":")[1].split(",")]
    op_tokens = lines[2].split("=")[1].split()

    def parse_operand(token):
        if token.strip() == "old":
            return -1
        else:
            return int(token)

    operands = [parse_operand(x) for x in op_tokens[::2]]
    op = add if op_tokens[1] == "+" else mul

    def last_int(l):
        return int(l.split()[-1])

    test = last_int(lines[3])
    targets = (last_int(lines[4]), last_int(lines[5]))

    return Monkey(items, operands, op, test, targets)


def parse(fname="input.txt"):
    monkeys = open(fname).read().split("\n\n")
    return [parse_monkey_str(s) for s in monkeys]


def run_monkeys(monkeys: list[Monkey], div: int, n: int):
    lcm = math.lcm(*[m.test for m in monkeys])
    
    inspection_counts = [0] * len(monkeys)

    def throw_to(item, target_idx):
        monkeys[target_idx].items.append(item)

    def do_turn(monkey_n):
        monkey = monkeys[monkey_n]
        inspection_counts[monkey_n] += len(monkey.items)
        for idx, item in enumerate(monkey.items):
            item = monkey.do_op(item)
            item = item % lcm
            item = item // div
            result = item % monkey.test == 0
            a, b = monkey.targets
            tgt = a if result else b
            throw_to(item, tgt)
        monkey.items = []

    def do_round():
        for idx, _ in enumerate(monkeys):
            do_turn(idx)

    for round in range(n):
        do_round()

    inspection_counts.sort()
    return inspection_counts[-2] * inspection_counts[-1]


def part1(monkeys):
    print(run_monkeys(monkeys, 3, 20))


def part2(monkeys):
    print(run_monkeys(monkeys, 1, 10000))


part1(parse("input.txt"))
part2(parse("input.txt"))
