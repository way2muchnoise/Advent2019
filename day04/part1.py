import re

with open('input.txt', 'r') as f:
    line = f.readline()
    start, end = map(int, line.split('-'))

double_digit = re.compile(r'(\d)\1')

valid_codes = []
for code in range(start, end+1):
    code_s = repr(code)
    if double_digit.search(code_s):
        if ''.join(sorted(list(code_s))) == code_s:
            valid_codes.append(code_s)
print len(valid_codes)
