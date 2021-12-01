from numpy import loadtxt, diff, ones, convolve

data = loadtxt('2021/data/day1.txt', dtype = int)


# My solution
def p1s1():
    count = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            count += 1
    return count


# Stolen solution
def p1s2():
    return sum(diff(data) > 0)


# My solution
def p2s1():
    count = 0
    for i in range(len(data) - 3):
        if (data[i + 1] + data[i + 2] + data[i + 3]) > (data[i] + data[i + 1] + data[i + 2]):
            count += 1
    return count
    

# Stolen solution
def p2s2():
    return sum(diff(convolve(data, ones(3), 'valid')) > 0)



print(p1s1())
print(p1s2())

print(p2s1())
print(p2s2())