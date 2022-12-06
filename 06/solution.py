#%%


def part1(fname="input.txt"):
    s = open(fname).read()
    return find_end_of_marker(s, 4)


def part2(fname="input.txt"):
    s = open(fname).read()
    return find_end_of_marker(s, 14)


def find_end_of_marker(s, n):
    for index in range(len(s) - n):
        slice = s[index : index + n]
        if len(set(slice)) == n:
            return index + n


print(part1())
print(part2())
