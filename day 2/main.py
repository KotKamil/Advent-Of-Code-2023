with open('data.txt') as file:
    input = file.read().split('\n')

cubes = {
    "blue": 14,
    "red": 12,
    "green": 13
}
def part_one(tab):
    sum = 0
    for (index, line) in enumerate(tab):
        gameId, game = line.split(':')
        gameId = gameId.split(' ')[1]
        sets = all(map(lambda set: all(map(lambda element: (cubes[element.split(' ')[2]]>=int(element.split(' ')[1])), set.split(','))), game.split(';')))
        if sets: sum += int(gameId)
    return sum

def part_two(tab):
    power = 0
    for (index, line) in enumerate(tab):
        maxValues = {'red': 0, 'green': 0, 'blue': 0}
        game = line.split(':')[1]
        sets = list(map(lambda set: list(map(lambda element: {element.split(' ')[2]: element.split(' ')[1]}, set.split(','))), game.split(';')))

        for set in sets:
            for element in set:
                for color, value in element.items():
                    maxValues[color] = max(maxValues[color], int(value))

        power += maxValues['red']*maxValues['green']*maxValues['blue']
    return power

# print(f'Part one solution: {part_one(input)}')
print(f'Part two solution: {part_two(input)}')