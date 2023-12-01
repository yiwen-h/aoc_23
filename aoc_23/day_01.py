from load_data import get_data

day = "01"


def part_1(data):
    # split data into list
    data_list = data.split("\n")
    numbers = "0123456789"
    num_list = []
    # iterate through list
    for each in data_list:
        # find first number
        for i in each:
            if i in numbers:
                first = i
                break
        # find last number
        for i in reversed(each):
            if i in numbers:
                last = i
                break
        # put numbers together
        num = first + last
        num = int(num)
        num_list.append(num)
    # add all the numbers together
    return sum(num_list)


### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f"part 1 solution = {part_1(raw_data)}")


def part_2(data):
    num_map = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    data_list = data.split("\n")
    num_list = []
    for each in data_list:
        # find first number
        is_looping = True
        for i in range(len(each)):
            for length in range(6):
                window = each[i:i+length]
                if window in num_map.keys():
                    is_looping = False
                    first = num_map[window]
                    break
            if not is_looping:
                break
        # find last number
        is_looping = True
        for endpoint in range(len(each), 0, -1):
            for startpoint in range(-6,0):
                window = each[startpoint+endpoint: endpoint]
                if window in num_map.keys():
                    is_looping = False
                    last = num_map[window]
                    break
            if not is_looping:
                break
        num = first + last
        num = int(num)
        num_list.append(num)
    return sum(num_list)

print(f"part 2 solution = {part_2(raw_data)}")