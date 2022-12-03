#%%
def priority(x: str):
    if x.capitalize() == x:
        return ord(x) - ord('A') + 27
    else:
        return ord(x) - ord('a') + 1


def eval_priority(line: str):
    if len(line) == 0:
        return 0
    l = len(line) // 2
    first = line[:l]
    second = line[l:]
    common, = list(set(first).intersection(set(second)))
    return priority(common)


def part1(fname='input.txt'):
    with open(fname, 'r') as f:
        print(sum([eval_priority(line) for line in f]))


def part2(fname='input.txt'):
    with open(fname, 'r') as f:
        s = f.read().split('\n')
    groups = list(zip(s[::3], s[1::3], s[2::3]))
    commons = [list(set.intersection(*[set(x) for x in g]))[0] for g in groups]
    print(sum((priority(ch) for ch in commons)))


part1()
part2()
