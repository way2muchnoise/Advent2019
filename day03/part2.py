with open('input.txt', 'r') as f:
    line = f.readline()
    wire1 = line.split(',')
    line = f.readline()
    wire2 = line.split(',')

board = {}


def get_direction(letter):
    if letter is 'U':
        return 1, 0
    elif letter is 'D':
        return -1, 0
    elif letter is 'L':
        return 0, -1
    elif letter is 'R':
        return 0, 1
    else:
        return 0, 0


wires = [wire1, wire2]
for w in range(0, len(wires)):
    position = [0, 0]
    steps = 0
    for path in wires[w]:
        direction = get_direction(path[0])
        count = int(path[1:])
        for i in range(0, count):
            position[0] += direction[0]
            position[1] += direction[1]
            key = ','.join(map(repr, position))
            if not board.has_key(key):
                board[key] = [0, 0]
            steps += 1
            board[key][w] = steps

crossings = []
for key in board.keys():
    value = board[key]
    if value[0] > 1 and value[1] > 1:
        crossings.append((key, value[0] + value[1]))

crossings = sorted(crossings, key=lambda c: c[1])
print crossings[0]
