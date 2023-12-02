from aoc_23 import day_02
from aoc_23.load_data import get_test_data


test_data = get_test_data('02')
expected_result_part_1 = 8


def test_part_1():
    assert day_02.part_1(test_data) == expected_result_part_1

test_data_b = get_test_data('02')
expected_result_part_2 = 2286

def test_part_2():
    assert day_02.part_2(test_data_b) == expected_result_part_2