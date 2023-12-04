from aoc_23 import day_04
from aoc_23.load_data import get_test_data


test_data = get_test_data('04')
expected_result_part_1 = 13


def test_part_1():
    assert day_04.part_1(test_data) == expected_result_part_1

# test_data_b = get_test_data('02')
# expected_result_part_2 = 2286

# def test_part_2():
#     assert day_03.part_2(test_data_b) == expected_result_part_2