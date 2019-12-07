import re

with open('input.txt', 'r') as f:
    line = f.readline()
    start, end = map(int, line.split('-'))

sequential_digits = re.compile(r'((\d)\2+)')

valid_codes = []
for code in range(start, end+1):
    code_s = repr(code)
    sequential = map(lambda t: t[0], sequential_digits.findall(code_s))
    if len(sequential) > 0 and filter(lambda sequence: len(sequence) == 2, sequential):
        if ''.join(sorted(list(code_s))) == code_s:
            valid_codes.append(code_s)
print len(valid_codes)
