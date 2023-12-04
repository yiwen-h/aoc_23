from load_data import get_data

day = "4"

def part_1(data):
    cards = data.split('\n')
    total_score = 0
    for card in cards:
        parts = card.split('|')
        winners = parts[0].split(':')[-1].strip().split(' ')
        winners = [int(winner) for winner in winners if winner != '']
        game_numbers = parts[1].split(' ')
        game_numbers = [int(game_num) for game_num in game_numbers if game_num != '']
        num_winners = 0
        for gn in game_numbers:
            if gn in winners:
                num_winners += 1
        card_score = 0
        if num_winners != 0:
            card_score = 1
        for i in range(num_winners-1):
            card_score *= 2
        total_score += card_score
    return total_score


### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f"part 1 solution = {part_1(raw_data)}")


def part_2(data):
    return None

# print(f"part 2 solution = {part_2(raw_data)}")