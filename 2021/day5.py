with open("day5.txt") as file:
    lines = file.readlines()

coords = {}

for line in lines:

    coordinates = line.strip().split(' -> ')

    start_x = int(coordinates[0].split(",")[0])
    start_y = int(coordinates[0].split(",")[1])
    finish_x = int(coordinates[1].split(",")[0])
    finish_y = int(coordinates[1].split(",")[1])

    if start_x == finish_x:
        if finish_y < start_y:
            finish_y, start_y = start_y, finish_y
        for i in range(start_y, finish_y + 1):
            try: 
                coords[(start_x, i)] += 1
            except:
                coords[(start_x, i)] = 1

    elif start_y == finish_y:
        if finish_x < start_x:
            finish_x, start_x = start_x, finish_x
        for i in range(start_x, finish_x + 1):
            try: 
                coords[(i, start_y)] += 1
            except:
                coords[(i, start_y)] = 1

    ### for part 2 ###
    elif (finish_y - start_y) == (finish_x - start_x):
        if finish_x < start_x:
            finish_x, start_x = start_x, finish_x

        if finish_y < start_y:
            finish_y, start_y = start_y, finish_y

        for i in range(finish_y - start_y + 1):
            try: 
                coords[(start_x + i, start_y + i)] += 1
            except:
                coords[(start_x + i, start_y + i)] = 1

    elif abs(finish_y - start_y) == abs(finish_x - start_x):
        if start_y > finish_y:
            for i in range(finish_x - start_x + 1):
                try: 
                    coords[(start_x + i, start_y - i)] += 1
                except:
                    coords[(start_x + i, start_y - i)] = 1

        if start_x > finish_x:
            for i in range(finish_y - start_y + 1):
                try: 
                    coords[(start_x - i, start_y + i)] += 1
                except:
                    coords[(start_x - i, start_y + i)] = 1
        ###

count = 0
for x in coords:
    if coords[x] > 1:
        count += 1

print(count)