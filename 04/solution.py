def fully_contained(i1, i2):
    x0, y0 = i1
    x1, y1 = i2
    return x0 <= x1 and y1 <= y0


def either_contains(i1, i2):
    return fully_contained(i1, i2) or fully_contained(i2, i1)


def do_they_overlap(i1, i2):
    if i1[0] > i2[0]:
        i2, i1 = i1, i2
    x_l, x_r = i1
    y_l, y_r = i2
    return x_r >= y_l


def parse_interval(interval_str: str):
    x, y = interval_str.split('-')
    return int(x), int(y)


def parse_line(line):
    i1, i2 = line.split(',')
    return parse_interval(i1), parse_interval(i2)


def part1(fname='input.txt'):
    with open(fname, 'r') as f:
        result = sum(int(either_contains(*parse_line(line))) for line in f)
    print(result)


def part2(fname='input.txt'):
    with open(fname, 'r') as f:
        result = sum(int(do_they_overlap(*parse_line(line))) for line in f)
    print(result)


part1()
part2()
