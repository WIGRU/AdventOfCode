with open("day11.txt") as file:
    lines = file.readlines()

octopus = {}

for y in range(len(lines)):
    for x in range(len(lines[y].strip())):
        octopus[(x,y)] = {'value': int(lines[y].strip()[x]), 'flashed': False}

#print(octopus)
steps = 1000000
flashes = []

def flash(k):
    if octopus[k]['value'] > 9 and octopus[k]['flashed'] == False:
        flashes.append(k)
        octopus[k]['flashed'] = True

        if (k[0] - 1, k[1]) in octopus.keys():
            octopus[(k[0] - 1, k[1])]['value'] += 1
            if octopus[(k[0] - 1, k[1])]['value'] > 9 and octopus[(k[0] - 1, k[1])]['flashed'] == False:
                flash((k[0] - 1, k[1]))

        if (k[0] - 1, k[1] - 1) in octopus.keys():
            octopus[(k[0] - 1, k[1] - 1)]['value'] += 1
            if octopus[(k[0] - 1, k[1] - 1)]['value'] > 9 and octopus[(k[0] - 1, k[1] - 1)]['flashed'] == False:
                flash((k[0] - 1, k[1] - 1))

        if (k[0] - 1, k[1] + 1) in octopus.keys():
            octopus[(k[0] - 1, k[1] + 1)]['value'] += 1
            if octopus[(k[0] - 1, k[1] + 1)]['value'] > 9 and octopus[(k[0] - 1, k[1] + 1)]['flashed'] == False:
                flash((k[0] - 1, k[1] + 1))

        if (k[0], k[1] + 1) in octopus.keys():
            octopus[(k[0], k[1] + 1)]['value'] += 1
            if octopus[(k[0], k[1] + 1)]['value'] > 9 and octopus[(k[0], k[1] + 1)]['flashed'] == False:
                flash((k[0], k[1] + 1))

        if (k[0], k[1] - 1) in octopus.keys():
            octopus[(k[0], k[1] - 1)]['value'] += 1
            if octopus[(k[0], k[1] - 1)]['value'] > 9 and octopus[(k[0], k[1] - 1)]['flashed'] == False:
                flash((k[0], k[1] - 1))

        if (k[0] + 1, k[1]) in octopus.keys():
            octopus[(k[0] + 1, k[1])]['value'] += 1
            if octopus[(k[0] + 1, k[1])]['value'] > 9 and octopus[(k[0] + 1, k[1])]['flashed'] == False:
                flash((k[0] + 1, k[1]))

        if (k[0] + 1, k[1] - 1) in octopus.keys():
            octopus[(k[0] + 1, k[1] - 1)]['value'] += 1
            if octopus[(k[0] + 1, k[1] - 1)]['value'] > 9 and octopus[(k[0] + 1, k[1] - 1)]['flashed'] == False:
                flash((k[0] + 1, k[1] - 1))

        if (k[0] + 1, k[1] + 1) in octopus.keys():
            octopus[(k[0] + 1, k[1] + 1)]['value'] += 1
            if octopus[(k[0] + 1, k[1] + 1)]['value'] > 9 and octopus[(k[0] + 1, k[1] + 1)]['flashed'] == False:
                flash((k[0] + 1, k[1] + 1))


for i in range(steps):
    for k in octopus.keys():
        octopus[k]['value'] += 1
        octopus[k]['flashed'] = False

    for k in octopus.keys():
        if octopus[k]['value'] > 9:
            flash(k)


    if all([octopus[k]['flashed'] for k in octopus.keys()]):
        print(i + 1)
        break

    for k in octopus.keys():
        if octopus[k]['flashed'] == True:
            octopus[k]['value'] = 0
            

print(len(flashes))