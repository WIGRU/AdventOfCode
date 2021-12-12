with open("day9.txt") as file:
    lines = file.readlines()

values = {} # all coordinates with their depth value
for y in range(len(lines)):
    for x in range(len(lines[y].strip())):
        values[(x, y)] = int(lines[y][x])


def get_lowpoints(values):
    lowpoints = {}

    for coordinate in values.keys(): 
        x, y = coordinate
        lowpoint = True

        coordsToCheck = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for ctc in coordsToCheck:
            if ctc in values.keys() and not values[coordinate] < values[ctc]:
                lowpoint = False

        if lowpoint:
            lowpoints[coordinate] = values[coordinate]
    
    return lowpoints
                

def part1():
    risk = 0
    lowpoints = get_lowpoints(values)

    for lp in lowpoints.keys():
        risk += lowpoints[lp] + 1

    return risk


def part2():
    basins = []
    lowpoints = get_lowpoints(values)
    
    basin = [] # list with coordinates part of basin
    def s(p): # function to find size of basin
        x, y = p
        if values[p] != 9:
            if p not in basin:
                basin.append(p)

                around = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
                for x in around:
                    if x in values.keys() and x not in basin:
                        s(x)
    
    for p in lowpoints:
        basin = [] # reset basin size
        s(p)
        basins.append(len(basin))
        
    basins.sort()
    basins.reverse()

    return basins[0] * basins[1] * basins[2]


print(part1())
print(part2())