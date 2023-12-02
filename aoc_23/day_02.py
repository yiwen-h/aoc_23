from load_data import get_data

day = "2"

def part_1(data):
    data_split = data.split('\n')
    max_balls = {'red': 12,'green': 13, 'blue': 14}
    valid_games = []
    for game in data_split:
        valid = True
        game_no = int(game.split(':')[0].replace('Game ', ''))
        rounds = game.split(':')[1].split(';')
        for round in rounds:
            balls = round.split(',')
            for each in balls:
                num_balls = each.strip().split(' ')
                colour = num_balls[1]
                if int(num_balls[0]) > max_balls[colour]:
                    valid = False
                    break
        if valid:
            valid_games.append(game_no)
    return sum(valid_games)


### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f"part 1 solution = {part_1(raw_data)}")


def part_2(data):
    # work out max of each colour of ball in each game
    data_split = data.split('\n')
    total_power = 0
    for game in data_split:
        balls_dict = {'red': 0, 'green': 0, 'blue': 0}
        rounds = game.split(':')[1].split(';')
        for round in rounds:
            balls = round.split(',')
            for each in balls:
                num_balls = each.strip().split(' ')
                colour = num_balls[1]
                if int(num_balls[0]) > balls_dict[colour]:
                    balls_dict[colour] = int(num_balls[0])
    # power of each game (max of each colour multiplied)
        game_power = 1
        for v in balls_dict.values():
            game_power *= v
    # sum of all gamepowers
        total_power += game_power
    return total_power

print(f"part 2 solution = {part_2(raw_data)}")