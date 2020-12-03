from functools import reduce

with open("input.txt") as f:
    data = f.read().strip()
    tree_map = []
    for line in data.split('\n'):
        tree_map.append([x == '#' for x in line])


def solve():
    map_horiz = len(tree_map[0])
    map_vert = len(tree_map)
    counts = []
    for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        count = 0
        pos = (0, 0)
        while True:
            pos = (pos[0] + slope[0], pos[1] + slope[1])
            if pos[0] >= map_vert:
                break
            count += tree_map[pos[0]][pos[1] % map_horiz]
        counts.append(count)
    print(counts[1])
    print(reduce(lambda x, y: x * y, counts, 1))


if __name__ == '__main__':
    solve()
