#%%


def part1(fname="input.txt"):
    states = [1]

    def parse_line(line):
        nonlocal states
        if line.strip() == "noop":
            states.append(states[-1])
        else:
            val = int(line.split()[-1])
            states.append(states[-1])
            states.append(states[-1] + val)

    with open(fname, "r") as f:
        for line in f:
            parse_line(line)

    indices = [20, 60, 100, 140, 180, 220]
    return sum(idx * states[idx - 1] for idx in indices)


def part2(fname="input2.txt"):
    states = [1]

    def parse_line(line):
        nonlocal states
        if line.strip() == "noop":
            states.append(states[-1])
        else:
            val = int(line.split()[-1])
            states.append(states[-1])
            states.append(states[-1] + val)

    with open(fname, "r") as f:
        for line in f:
            parse_line(line)

    idx = 1
    for ii in range(240 // 40):
        for jj in range(40):
            if abs(idx % 40 - states[idx]) <= 1:
                print("#", end="")
            else:
                print(".", end="")
            idx += 1
        print("\n", end="")


part1("input.txt")
part2("input.txt")
