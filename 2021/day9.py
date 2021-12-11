with open("day9.txt") as file:
    lines = file.readlines()


def part1():
    risk = 0
    coords = {}
    for y in range(len(lines)):
        for x in range(len(lines[y].strip())):
            coords[(x, y)] = int(lines[y][x])

    for c in coords.keys():
        x = c[0]
        y = c[1]
        lowpoint = True
        if (x + 1, y) in coords.keys():
            if not coords[c] < coords[(x + 1, y)]:
                lowpoint = False

        if (x - 1, y) in coords.keys():
            if not coords[c] < coords[(x - 1, y)]:
                lowpoint = False

        if (x, y + 1) in coords.keys():
            if not coords[c] < coords[(x, y + 1)]:
                lowpoint = False

        if (x, y - 1) in coords.keys():
            if not coords[c] < coords[(x, y - 1)]:
                lowpoint = False

        if lowpoint:
            risk += coords[c] + 1
            print(x,y)

    return risk


#print(part1())


def part2():
    coords = {}
    for y in range(len(lines)):
        for x in range(len(lines[y].strip())):
            coords[(x, y)] = int(lines[y][x])


    basin = set()

    def recur(x, y):
        print(len(basin))
        if coords[(x, y)] == 9:
            pass
        else:
            basin.add((x, y))

            if x > 1:
                recur(x - 1, y)
            if x < (len(lines[y].strip()) - 1):
                recur(x + 1, y)
            if y < (len(lines) - 1):
                recur(x, y + 1)

    recur(8, 0)

    print(len(basin))


print(part2())

from termcolor import colored

with open("day9.txt") as file:
    lines = file.readlines()

'''
for y in range(len(lines)):
    for x in range(len(lines[y].strip())):
        if int(lines[y][x]) == 9:
            print(colored('9', 'red'), end="")
        else:
            print(lines[y][x], end="")
    print("")
'''