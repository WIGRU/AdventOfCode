with open("day12.txt") as file:
    lines = file.readlines()


def part1():
    caves = [x.strip().split("-") for x in lines]

    paths = []
    def find(path):
        latest = path.split("-")[-1] # get latest cave in path

        next = [] # options from current loc
        for cave in caves:
            if cave[0] == latest:
                next.append(cave[1])
            if cave[1] == latest:
                next.append(cave[0])

        for n in next:
            if n == 'end':
                paths.append(path + '-end')
            
            elif n != 'start' and n.lower() not in path:
                find(path + '-' + n)
    
    find('start')
    return len(paths)


def part2():
    caves = [x.strip().split("-") for x in lines]

    lowercaves = set()
    for x in lines:
        for i in x.strip().split("-"):
            if i.islower():
                lowercaves.add(i)

    paths = []
    def find(path):
        latest = path.split("-")[-1] # get latest cave in path

        next = [] # options from current loc
        for cave in caves:
            if cave[0] == latest:
                next.append(cave[1])
            if cave[1] == latest:
                next.append(cave[0])

        for n in next:
            doubles = 0
            for x in lowercaves:
                if (path + '-' + n).count(x.lower()) == 2:
                    doubles += 1
                elif (path + '-' + n).count(x.lower()) > 2:
                    doubles += 2

            if n == 'end':
                paths.append(path + '-end')
            
            elif n != 'start' and not doubles > 1:
                find(path + '-' + n)
    
    find('start')
    return len(paths)



print(part1())
print(part2())
