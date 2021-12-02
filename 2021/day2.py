import re

filename = '2021/data/day2.txt'


def input_as_string(filename):
    with open(filename) as f:
        string = f.read().replace("\n","")
    return string


def p1(moves):
    horizontal = depth = 0
    for move in moves:
        if move[0] == "forward":
            horizontal += int(move[1])
        elif move[0] == "up":
            depth -= int(move[1])
        elif move[0] == "down":
            depth += int(move[1])

    return horizontal*depth


def p2(moves):
    horizontal = depth = aim = 0
    for move in matches:
        if move[0] == "forward":
            horizontal += int(move[1])
            depth += int(move[1]) * aim
        elif move[0] == "up":
            aim -= int(move[1])
        elif move[0] == "down":
            aim += int(move[1])

    return horizontal*depth


s = input_as_string(filename)

matches = re.findall(r'(\w+) (\d+)', s)

print(p1(matches))
print(p2(matches))