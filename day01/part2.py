import math

total_fuel = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        mass = int(line)
        fuel = math.floor(mass / 3) - 2
        while fuel > 0:
            total_fuel += fuel
            fuel = math.floor(fuel / 3) - 2
        line = f.readline()
print total_fuel
