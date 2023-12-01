with open('data.txt') as file:
    input = file.read().split('\n')

#My solution to part 1
def part_one(tab):
    lineNumbers = []
    for line in tab:
        left, right = '0', '0'
        for character in list(line):
            try:
                int(character)
                left = character
                break
            except:
                pass

        for character in reversed(list(line)):
            try:
                int(character)
                right = character
                break
            except:
                pass

        lineNumbers.append(int(str(left + right)))

    sum = 0
    for num in lineNumbers:
        sum += num
    return sum

#My solution to part 2
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
def part_two(tab):
    lineNumbers = []
    for line in tab:
        leftIndex, rightIndex = len(line), -1
        left, right = '0', '0'
        def searchForFirstKey(keys, firstIndex):
            bestKey = left
            for key in keys:
                index = line.find(key)
                if index != -1 and index < firstIndex:
                    firstIndex = index
                    bestKey = key
            return firstIndex, bestKey

        leftIndex, left = searchForFirstKey(numbers.values(), leftIndex)
        left = next((k for k, v in numbers.items() if v == left), None)
        leftIndex, left = searchForFirstKey(numbers, leftIndex)

        def searchForLastKey(keys, lastIndex):
            bestKey = right
            for key in keys:
                index = line.rfind(key)
                if index != -1 and index > lastIndex:
                    lastIndex = index
                    bestKey = key
            return lastIndex, bestKey

        rightIndex, right = searchForLastKey(numbers.values(), rightIndex)
        right = next((k for k, v in numbers.items() if v == right), None)
        rightIndex, right = searchForLastKey(numbers, rightIndex)

        lineNumbers.append(int(str(left + right)))

    sum = 0
    for num in lineNumbers:
        sum += num
    return sum


print(f'Part one solution: {part_one(input)}')
print(f'Part two solution: {part_two(input)}')
