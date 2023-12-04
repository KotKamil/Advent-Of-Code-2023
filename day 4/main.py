import math

with open('data.txt') as file:
    data = file.read().split('\n')


def part_one(tab):
    points = 0
    for line in data:
        winning_numbers, my_numbers = line.split(':')[1].split('|')[0].split(), line.split(':')[1].split('|')[1].split()
        card_power = -1
        for my_number in my_numbers:
            if my_number in winning_numbers:
                card_power += 1
        points += math.floor(2**card_power)
    return points


def part_two(tab):
    return scratch_card(tab, 0, [0 for _ in tab], 0)


def scratch_card(tab, current_card, copies, score):
    line = tab[current_card]
    winning_numbers, my_numbers = line.split(':')[1].split('|')[0].split(), line.split(':')[1].split('|')[1].split()
    matches = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            matches += 1
    score += copies[current_card] + 1
    if current_card >= len(tab) - 1:
        return score
    for i in range(current_card + 1, current_card + matches + 1):
        copies[i] += 1 + copies[current_card]
    return scratch_card(tab, current_card + 1, copies, score)


# print(f"Part one solution: {part_one(data)}")
print(f"Part one solution: {part_two(data)}")
