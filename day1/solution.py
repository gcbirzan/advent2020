with open("input.txt") as f:
    data = f.read()


def solve():
    values = set(int(x) for x in data.split('\n') if x)
    for x in values:
        if 2020 - x in values:
            print(x * (2020 - x))
            break
    values_list = list(values)
    for idx, i in enumerate(values_list):
        for j in values_list[idx + 1:]:
            if 2020 - (i + j) in values:
                print(i * j * (2020 - (i + j)))
                return


if __name__ == '__main__':
    solve()
