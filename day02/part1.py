intcode_program = []
with open('input.txt', 'r') as f:
    line = f.readline()
    intcode_program = map(int, line.split(','))

intcode_program[1] = 12
intcode_program[2] = 2

pointer = 0
halt = False

while not halt:
    if intcode_program[pointer] is 1:
        intcode_program[intcode_program[pointer+3]] \
            = intcode_program[intcode_program[pointer+1]] + intcode_program[intcode_program[pointer+2]]
    elif intcode_program[pointer] is 2:
        intcode_program[intcode_program[pointer + 3]] \
            = intcode_program[intcode_program[pointer + 1]] * intcode_program[intcode_program[pointer + 2]]
    elif intcode_program[pointer] is 99:
        halt = True

    pointer += 4

print intcode_program[0]
