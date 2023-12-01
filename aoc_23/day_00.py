from load_data import get_data
from itertools import combinations
day = 00

## Using 2020 Day 1 as an example
## https://adventofcode.com/2020/day/1

def part_1(data):
    # split data into vector/list of numbers
    numbers = data.split('\n')
    # turn strings into numbers
    numbers_nums = [int(num) for num in numbers]
    # get all the possible pairs of numbers from my list
    pairs = list(combinations(numbers_nums, 2))
    # work out which pair adds to 2020
    for pair in pairs:
        if sum(pair) == 2020:
    # multiply that pair    
            answer = pair[0] * pair[1]
    return answer

### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f'part 1 solution = {part_1(raw_data)}')

def part_2(data):
    pass


