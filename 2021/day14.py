import itertools

with open("2021/data/day14.txt") as file:
    lines = file.readlines()

split = False
string = ""
instructions = {}
chars = set()

for line in lines:
    if line == "\n": 
        split = True
    elif split:
        value = line.split(" -> ")[1].strip()
        instructions[line.split(" -> ")[0]] = value
        chars.add(value)
    else:
        string = line.strip()


def part1(string):
    new_str = []

    for x in range(10):
        new_str = list(string)
        added = 0

        for i in range(len(string) - 1):
            if string[i] + string[i + 1] in instructions.keys():
                new_str.insert(i + 1 + added, instructions[string[i] + string[i + 1]])
                added += 1

        string = ''.join(str(elem) for elem in new_str)

    count = set()
    for c in chars:
        count.add(new_str.count(c))

    return max(count) - min(count)
        

def part2(string):
    polymer_list = {} # To keep track of possible combination of two chars
    char_count = {} # To count how often each char appears

    for x in chars: 
        char_count[x] = 0

    for x in chars:
        for y in chars:
            polymer_list[x + y] = 0

    for a in range(len(string) - 1):
        polymer_list[string[a] + string[a + 1]] += 1
    
    for a in string:
        char_count[a] += 1

    def tc():
        to_change = {}
        for x in chars:
            for y in chars:
                to_change[x + y] = 0
        return to_change

    for y in range(40):
        to_change = tc()
        for i in instructions:
            if polymer_list[i] > 0:
                to_change[i] -= polymer_list[i]
                char_count[instructions[i]] += polymer_list[i]
                to_change[i[0] + instructions[i]] += polymer_list[i]
                to_change[instructions[i] + i[1]] += polymer_list[i]

        for t in to_change:
            polymer_list[t] += to_change[t]

    countset = set()
    for c in char_count:
        countset.add(char_count[c])

    return max(countset) - min(countset)
    

print(part1(string))
print(part2(string))
