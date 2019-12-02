with open('input.txt', 'r') as f:
    line = f.readline()
    intcode_program_original = map(int, line.split(','))

for noun in range(0, 100):
    for verb in range(0, 100):

        intcode_program = intcode_program_original[:]
        intcode_program[1] = noun
        intcode_program[2] = verb

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

        if intcode_program[0] == 19690720:
            print "noun: " + repr(noun)
            print "verb: " + repr(verb)
            print 100 * noun + verb
            exit(0)
