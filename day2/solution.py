import re

with open("input.txt") as f:
    data = f.read().strip()
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    password_requirements = []
    for line in data.split('\n'):
        groups = pattern.match(line).groups()
        password_requirements.append((int(groups[0]), int(groups[1]), groups[2], groups[3]))

def solve():
    correct = 0
    for line in password_requirements:
        count = sum(1 for x in line[3] if x == line[2])
        if line[0] <= count <= line[1]:
            correct += 1
    print(correct)

    correct = 0
    for line in password_requirements:
        if (line[3][line[0] - 1] == line[2]) + (line[3][line[1] - 1] == line[2]) == 1:
            correct += 1

    print(correct)

if __name__ == '__main__':
    solve()

