import re

with open("input.txt") as f:
    data = f.read().strip()
pattern = re.compile(r'(\w{3}):([^$ ]*)')
passports = []
fields = set()
for passport in data.split('\n\n'):
    passport = passport.replace('\n', ' ')
    passport_data = dict(re.findall(pattern, passport))
    fields.update(passport_data)
    passports.append(passport_data)

required_fields = fields - {'cid'}

height_pattern = re.compile(r'(\d+)(in|cm)')
hair_pattern = re.compile(r'^#[0-9a-f]{6}$')
passport_number = re.compile(r'^\d{9}$')


def height_validate(value):
    match = re.match(height_pattern, value)
    if not match:
        return False
    number, unit = match.groups()
    number = int(number)
    if unit == 'in':
        return 59 <= number <= 76
    else:
        return 150 <= number <= 193


rules = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    # 'hgt': lambda x: 150 <= (int(x[:-2]) if x[-2:] == 'cm' else round(int(x[:-2]) * 2.54) if x[-2:] == 'in' else 0) <= 193,
    'hgt': height_validate,
    'hcl': lambda x: re.search(hair_pattern, x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.search(passport_number, x),
    'cid': lambda x: True,
}


def solve():
    valid = sum(1 for passport in passports if not required_fields.difference(passport))
    print(valid)
    valid = 0
    for passport in passports:
        if required_fields.difference(passport):
            continue
        for k, v in passport.items():
            if not rules[k](v):
                break
        else:
            valid += 1
    print(valid)


if __name__ == '__main__':
    solve()
