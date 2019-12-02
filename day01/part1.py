import math

total_fuel = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        mass = int(line)
        fuel = math.floor(mass/3) - 2
        total_fuel += fuel
        line = f.readline()
print total_fuel
