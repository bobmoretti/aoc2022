#%%
import numpy as np


def parse_elves(x):
    sublists = x.split('\n\n')
    return [[int(x) for x in sub.split()] for sub in sublists]


def get_sums(elf_data):
    return [np.sum(calories) for calories in elf_data]


def part1(infile='input.txt'):
    input = open(infile, 'r').read()
    return np.max(get_sums(parse_elves(input)))


def part2(infile='input.txt'):
    input = open(infile, 'r').read()
    totals = sorted(get_sums(parse_elves(input)))
    return sum(totals[-3:])

# %%
print(f'{part1()=}')
print(f'{part2()=}')
# %%
