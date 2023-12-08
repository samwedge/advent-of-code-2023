import io
import textwrap

import pytest

from aoc.day1_pt1 import extract_calibration_value


@pytest.fixture
def test_file():
    test_data = textwrap.dedent(
        """\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
    )
    f = io.StringIO(test_data)
    f.seek(0)
    return f


def test_extract_calibration_value(test_file):
    result = extract_calibration_value(test_file)
    assert result == 142
