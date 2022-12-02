#%%
import numpy as np


def parse_input(fname):
    m1_lookups = {'A': 1, 'B': 2, 'C': 3}
    m2_lookups = {'X': 1, 'Y': 2, 'Z': 3}
    with open(fname) as s:

        def parse_line(line):
            m1, m2 = line.split()
            return m1_lookups[m1], m2_lookups[m2]

        return [parse_line(l) for l in s]


def evaluate_rps(m1, m2):
    diff = m2 - m1
    if diff < 0:
        diff += 3

    if diff == 0:
        return 3
    if diff == 1:
        return 6
    return 0


def evaluate_move(m1, m2):
    rps_score = evaluate_rps(m1, m2)
    return rps_score + m2


def evaluate_moves(moves):
    return [evaluate_move(m1, m2) for m1, m2 in moves]


def part1(fname='input.txt'):
    moves = parse_input(fname)
    return np.sum(evaluate_moves(moves))


# Factors to add
# X == 1 == lose
# 1 -> 2
# Y == 2 == draw
# 2 -> 0
# Z == 3 == win
# 3 -> 1
def get_offset(m2):
    return (m2 + 1) % 3


def find_moves_for_desired_outcome(m1, m2):
    offset = get_offset(m2)
    m2 = m1 + offset
    if m2 < 1:
        m2 += 3
    if m2 > 3:
        m2 -= 3
    return m1, m2


def part2(fname='input.txt'):
    guide = parse_input(fname)
    moves = [find_moves_for_desired_outcome(m1, m2) for m1, m2 in guide]
    return np.sum(evaluate_moves(moves))


# %%
print(f'{part1()=}')
print(f'{part2()=}')
# %%
# %%
# %%

# %%
