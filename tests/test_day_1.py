from aoc_23 import day_01
from aoc_23.load_data import get_test_data


test_data = get_test_data('01')
expected_result_part_1 = 142


def test_part_1():
    assert day_01.part_1(test_data) == expected_result_part_1

test_data_b = get_test_data('01b')
expected_result_part_2 = 281

def test_part_2():
    assert day_01.part_2(test_data_b) == expected_result_part_2