import re

with open("day4.txt") as file:
    data = file.read()

    
instructions =  list(map(int, data.split("\n")[0].strip().split(",")))

boards = data.split("\n\n")[1:]
boards = [board.split("\n") for board in boards]
boards = [[ list(map(int, re.sub(' +', ' ', row.strip()).split(" "))) for row in board] for board in boards]

boards_score = []

for board in boards:
    score = []
    
    for row in board:
        for l in range(1, len(instructions)):
            bingo = True
            for x in row:
                if x not in instructions[0:l]:
                    bingo = False
            if bingo == True:
                score.append(l)

    for column in range(len(board[0])):
        for l in range(1, len(instructions)):
            bingo = True
            for row in board:
                if row[column] not in instructions[0:l]:
                    bingo = False
            if bingo == True:
                score.append(l)
    
    boards_score.append(min(score))

d = dict(enumerate(boards_score))

#key = min(d, key = d.get)
key = max(d, key = d.get)

nums = []
for row in boards[key]:
    for num in row:
        nums.append(num)

for i in instructions[0:d[key]]:
    try:
        nums.remove(i)
    except:
        pass

print(sum(nums)*instructions[d[key] - 1])