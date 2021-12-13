with open("day13.txt") as file:
    lines = file.readlines()
  
coords = set() 
ins = False
instructions = []

for line in lines:
    if line == "\n":
        ins = True
    elif ins:
        instructions.append(line.split(" ")[2].strip())
    else:
        c = line.split(",")
        coords.add((int(c[0]), int(c[1])))

for ins in instructions:
    new_coords = set()
    axis, line = ins.split("=")
    
    if axis == "x":
        a = 0
    else:
        a = 1
       
    for coord in coords:
        if coord[a] > int(line):
            x, y = coord
            if a == 1:
                new_coords.add((x, int(line) - (y - int(line))))
            else:
                new_coords.add((int(line) - (x - int(line)), y))
        else:
            new_coords.add(coord)
    
    print(len(new_coords))
    coords = new_coords

for y in range(int(line)):
    for x in range(40):
        if (x,y) in new_coords:
            print("⬛️", end=" ")
        else:
            print("  ", end=" ")
            pass
    print("\n")
