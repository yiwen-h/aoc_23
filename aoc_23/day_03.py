from load_data import get_data
import re

day = "3"

def part_1(data):
    not_symbols = '0123456789.'
    # find the numbers
    lines = data.split('\n')
    regex = r"\d+" 
    total = 0
    # for l in range(7,8):
    for l in range(len(lines)):
        line = lines[l]
        numbers = re.findall(regex, line)
        for num in numbers:
    # get coordinates of nums
            m = re.search(fr'\b{num}\b', line)        
            start = m.start()
            end = m.end()
            neighbours = ''
    # check above
            if l != 0:
                above = lines[l-1][start:end]
                neighbours += above                
    # check below
            if l < len(lines) -1:
                below = lines[l + 1][start:end]
                neighbours += below
    # check right
            if end < len(line):
                right = line[end]
                neighbours += right
    # check left
            if start > 0:
                left = line[start-1]
                neighbours += left

    # check up left
            if l != 0 and start > 0:
                up_left = lines[l-1][start-1]
                neighbours += up_left
    # check up right
            if l != 0 and end < len(line):
                up_right = lines[l-1][end]
                neighbours += up_right
    # check down left
            if l < len(lines) -1 and start > 0:
                down_left = lines[l + 1][start-1]
                neighbours += down_left
    # check down right
            if l < len(lines) -1 and end < len(line):
                down_right = lines[l + 1][end]
                neighbours += down_right
    # check if any neighbours are symbols
            for n in neighbours:
                if n not in not_symbols:
                    total += int(num)
                    break
    return total


### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f"part 1 solution = {part_1(raw_data)}")


def part_2(data):
    # find gears in a line
    # get coordinates of gear
    # check if neighbours are numbers
    # if yes - use re.search to find full number
    return None

# print(f"part 2 solution = {part_2(raw_data)}")