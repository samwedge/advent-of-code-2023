import io
import textwrap

import pytest

from aoc.day1_pt2 import extract_calibration_value


@pytest.fixture
def test_file():
    test_data = textwrap.dedent(
        """\
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
    )
    f = io.StringIO(test_data)
    f.seek(0)
    return f


@pytest.fixture
def test_file_nothing_to_swap():
    f = io.StringIO("123")
    f.seek(0)
    return f


@pytest.fixture
def test_file_with_merged_numbers():
    f = io.StringIO("ninenineight")
    f.seek(0)
    return f


@pytest.fixture
def test_file_with_merged_numbers_again():
    f = io.StringIO("nineight")
    f.seek(0)
    return f


@pytest.fixture
def test_file_with_more_than_one_instance_of_word():
    f = io.StringIO("seven8seven")
    f.seek(0)
    return f


def test_extract_calibration_value(test_file):
    result = extract_calibration_value(test_file)
    assert result == 281


def test_extract_calibration_value_when_nothing_to_find(test_file_nothing_to_swap):
    result = extract_calibration_value(test_file_nothing_to_swap)
    assert result == 13


def test_extract_calibration_value_with_merged_numbers(test_file_with_merged_numbers):
    result = extract_calibration_value(test_file_with_merged_numbers)
    assert result == 98


def test_extract_calibration_value_with_merged_numbers_again(test_file_with_merged_numbers_again):
    result = extract_calibration_value(test_file_with_merged_numbers_again)
    assert result == 98


def test_extract_calibration_value_with_more_than_one_instance_of_word(test_file_with_more_than_one_instance_of_word):
    result = extract_calibration_value(test_file_with_more_than_one_instance_of_word)
    assert result == 77
