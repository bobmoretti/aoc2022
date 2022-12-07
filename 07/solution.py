#%%
import numpy as np


def parse_dirtree(fname="input.txt"):
    with open(fname) as f:
        return parse_tree(f)


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        # self.leaf_size = 0
        self.total_size = 0
        self.parent = parent
        self.subdirs = {}

    def add_leaf(self, size):
        self.total_size += size

    def add_directory(self, name):
        self.subdirs[name] = Directory(name, self)

    def __repr__(self):
        return f"Directory {self.name} with size {self.total_size}"


def parse_tree(lines):

    cur = Directory("/")
    root = cur

    small_dir_total = 0

    def parse_command(command):
        nonlocal cur, small_dir_total
        if command.startswith("$ ls"):
            pass
        elif command.startswith("$ cd"):
            dest = command.split()[-1].strip()
            if dest == "/":
                cur = root
            elif dest == "..":
                if cur.total_size <= 100000:
                    small_dir_total += cur.total_size
                cur.parent.total_size += cur.total_size
                cur = cur.parent
            else:
                cur = cur.subdirs[dest]
        elif command.startswith("dir"):
            cur.add_directory(command.split()[-1])
        else:
            cur.add_leaf(int(command.split()[0]))

    for line in lines:
        parse_command(line)

    # unwind
    while cur.parent is not None:
        cur.parent.total_size += cur.total_size
        cur = cur.parent

    return root, small_dir_total


def part1(fname="input.txt"):
    print(parse_dirtree(fname)[1])


def part2(fname="input.txt"):
    root = parse_dirtree(fname)[0]
    sizes = []

    def add_size(node: Directory):
        assert node.total_size is not None
        sizes.append(node.total_size)
        for n in node.subdirs:
            add_size(node.subdirs[n])

    add_size(root)

    total_space = 70000000
    used = root.total_size
    free = total_space - used
    need_to_free = 30000000 - free
    sizes.sort()
    sizes = np.array(sizes)
    return sizes[np.where(sizes >= need_to_free)][0]
