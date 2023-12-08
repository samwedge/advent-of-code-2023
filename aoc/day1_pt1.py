import re
from typing import IO


def extract_calibration_value(f: IO) -> int:
    lines = f.readlines()
    just_numbers = [re.findall(r'\d', line) for line in lines]
    return sum(int(n[0] + n[-1]) for n in just_numbers)


if __name__ == '__main__':
    with open('../data/day1.txt') as f:
        print(extract_calibration_value(f))
