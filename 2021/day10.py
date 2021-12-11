import statistics

with open("day10.txt") as file:
    lines = file.readlines()

score = 0
scores = []
for line in lines:
    left = '([{<'
    right = ')]}>'
    point = {')': 3, ']': 57, '}': 1197, '>': 25137}
    point2 = {'(': 1, '[': 2, '{': 3, '<': 4}

    repl = ['()', '[]', '{}', '<>']
    for i in line:
        for x in repl:
            line = line.replace(x, '')

    corrupted = False
    for i in range(len(line) - 1):
        if line[i] in left and line[i + 1] in right:
            score += point[line[i + 1]]
            corrupted = True

    if not corrupted:
        score2 = 0
        line = line.strip()[::-1] #Reverse
        for i in range(len(line.strip())):
            score2 = (score2 * 5) + point2[line[i]]

        scores.append(score2)

print(score)
print(statistics.median(scores))