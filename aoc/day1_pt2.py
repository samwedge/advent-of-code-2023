import re
from typing import IO


MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def extract_calibration_value(f: IO) -> int:
    lines = f.readlines()
    return sum(find_calibration_number_for_line(line) for line in lines)


def find_calibration_number_for_line(line: str) -> int:
    indexes = {
        **{
            index: number_value
            for number_string, number_value in MAPPING.items()
            if (index := line.find(number_string)) != -1
        },
        **{
            index: number_value
            for number_string, number_value in MAPPING.items()
            if (index := line.rfind(number_string)) != -1
        },
        **{
            index: number_value
            for _, number_value in MAPPING.items()
            if (index := line.find(number_value)) != -1
        },
        **{
            index: number_value
            for _, number_value in MAPPING.items()
            if (index := line.rfind(number_value)) != -1
        },
    }

    leftmost = indexes[min(indexes)]
    rightmost = indexes[max(indexes)]

    return int(leftmost + rightmost)


if __name__ == '__main__':
    with open('../data/day1.txt') as f:
        print(extract_calibration_value(f))
