def part1(days):
    school = list(map(int, open("day6.txt").readlines()[0].split(",")))
    for i in range(days):
        for fish in range(len(school)):
            school[fish] -= 1

            if school[fish] == -1:
                    school[fish] = 6
                    school.append(8)

    return len(school)


def part2(days):
    school_dict = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    
    for num in list(map(int, open("day6.txt").readlines()[0].split(","))):
        school_dict[num] += 1

    for i in range(days):
        for x in range(-1, 8):
            school_dict[x] += school_dict[x + 1]
            school_dict[x + 1] = 0
        school_dict[8] += school_dict[-1]
        school_dict[6] += school_dict[-1]
        school_dict[-1] = 0
        
    return school_dict[0] + school_dict[1] + school_dict[2] + school_dict[3] + school_dict[4] + school_dict[5] + school_dict[6] +school_dict[7] +school_dict[8]


print(part1(80))
print(part2(256))