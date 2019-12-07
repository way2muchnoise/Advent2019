with open('input.txt', 'r') as f:
    line = f.readline()
    intcode_program = map(int, line.split(','))


def get_value(value, mode):
    return intcode_program[value] if mode == 0 else value


pointer = 0
halt = False

while not halt:
    instruction = repr(intcode_program[pointer]).zfill(5)
    opcode = int(instruction[-2:])
    m1, m2, m3 = reversed(map(int, list(instruction[0:-2])))
    if opcode == 1:
        intcode_program[intcode_program[pointer+3]] = get_value(intcode_program[pointer+1], m1) + get_value(intcode_program[pointer+2], m2)
        pointer += 4
    elif opcode == 2:
        intcode_program[intcode_program[pointer+3]] = get_value(intcode_program[pointer+1], m1) * get_value(intcode_program[pointer+2], m2)
        pointer += 4
    elif opcode == 3:
        intcode_program[intcode_program[pointer+1]] = int(input('Give input: '))
        pointer += 2
    elif opcode == 4:
        print get_value(intcode_program[pointer+1], m1)
        pointer += 2
    elif opcode == 5:
        if get_value(intcode_program[pointer+1], m1) != 0:
            pointer = get_value(intcode_program[pointer+2], m2)
        else:
            pointer += 3
    elif opcode == 6:
        if get_value(intcode_program[pointer+1], m1) == 0:
            pointer = get_value(intcode_program[pointer+2], m2)
        else:
            pointer += 3
    elif opcode == 7:
        intcode_program[intcode_program[pointer+3]] = int(get_value(intcode_program[pointer+1], m1) < get_value(intcode_program[pointer+2], m2))
        pointer += 4
    elif opcode == 8:
        intcode_program[intcode_program[pointer+3]] = int(get_value(intcode_program[pointer+1], m1) == get_value(intcode_program[pointer+2], m2))
        pointer += 4
    elif opcode == 99:
        halt = True

print 'End'
