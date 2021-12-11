with open("day3.txt") as file:
    lines = file.read().split("\n")


def part1():
    gamma = ""
    epsilon = ""

    for i in range(len(lines[0])):
        zeros = [line[i] for line in lines].count('0')
        ones = [line[i] for line in lines].count('1')
            
        if zeros > ones:
            gamma += "0"
        else:
            gamma += "1"

        if zeros < ones:
            epsilon += "0"
        else:
            epsilon += "1"


    return int(gamma, 2) * int(epsilon, 2)


def part2():
    with open("day3.txt") as file:
        lines = file.read().split("\n")

    for i in range(len(lines[0])):
        z = [line[i] for line in lines].count('0')
        o = [line[i] for line in lines].count('1')

        removed = True
        while removed:
            removed = False
            for line in lines:
                if z > o:
                    if line[i] == "1":
                        lines.remove(line)
                        removed = True
                else:
                    if line[i] == "0":
                        lines.remove(line)
                        removed = True

        if len(lines) == 1:
            oxygen = int(lines[0], 2)
            break

    with open("day3.txt") as file:
        lines = file.read().split("\n")

    for i in range(len(lines[0])):
        z = [line[i] for line in lines].count('0')
        o = [line[i] for line in lines].count('1')
        
        removed = True
        while removed:
            removed = False
            for line in lines:
                if o < z:
                    if line[i] == "0":
                        lines.remove(line)
                        removed = True
                else:
                    if line[i] == "1":
                        lines.remove(line)
                        removed = True

        if len(lines) == 1:
            c02 = int(lines[0], 2)
            break

    return oxygen * c02



print(part1())
print(part2())