from aoc_23 import day_00
from aoc_23.load_data import get_test_data


test_data = get_test_data(00)
expected_result_part_1 = 514579


def test_part_1():
    assert day_00.part_1(test_data) == expected_result_part_1
