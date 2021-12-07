with open("day7.txt") as file:
    data = file.readlines()[0].strip().split(",")

crabs = list(map(int, data))

fuel_1 = 0
fuel_2 = 0
for i in range(len(crabs)):
    tmp_fuel_1 = 0
    tmp_fuel_2 = 0
    for crab in crabs:
        tmp_fuel_1 += abs(crab - i)
        tmp_fuel_2 += sum(range(abs(crab-i)+1))

    if tmp_fuel_2 < fuel_2 or fuel_2 == 0:
        fuel_2 = tmp_fuel_2

    if tmp_fuel_1 < fuel_1 or fuel_1 == 0:
        fuel_1 = tmp_fuel_1

print(fuel_1)
print(fuel_2)

    