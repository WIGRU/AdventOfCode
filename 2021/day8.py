with open("day8.txt") as file:
    lines = file.readlines()

def part1():
    find = [2, 3, 4, 7]
    count = 0

    for line in lines:
        for pattern in line.split("|")[1].strip().split(" "):
            if len(pattern.strip()) in find:
                count += 1

    return count



def part2():

    total = 0

    for line in lines:
        input = line.strip().split("|")
        input = [x.strip().split(" ") for x in input]
        
        digits = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        five = []
        six = []
        for pattern in input[0]:
            if len(pattern) == 2:  digits[1] = set(pattern)
            if len(pattern) == 3:  digits[7] = set(pattern)
            if len(pattern) == 4:  digits[4] = set(pattern)
            if len(pattern) == 5:  five.append(pattern)
            if len(pattern) == 6:  six.append(pattern)
            if len(pattern) == 7:  digits[8] = set(pattern)


        for i in five:
            if digits[1].issubset(set(i)):
                digits[3] = set(i)
            elif digits[4].difference(digits[1]).issubset(set(i)):
                digits[5] = set(i)
            else:
                digits[2] = set(i)


        for i in six:
            middle = digits[4].difference(digits[1]).intersection(digits[3])

            if not digits[1].issubset(set(i)):
                digits[6] = set(i)
            elif middle.issubset(set(i)):
                digits[9] = set(i)
            else:
                digits[0] = set(i)


        value = ""
        for pattern in input[1]:
            for key in digits.keys():
                if digits[key] == set(pattern):
                    value += str(key)

        total += int(value)

            
    return(total)



print(part1())
print(part2())