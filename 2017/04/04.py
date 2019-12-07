def solve(input):
    seen = set()
    words = input.split()
    uniq = [x for x in input.split(' ') if x not in seen and not seen.add(x)]
    return len(uniq) is len(input.split(' '))


grade_sheet = [
    ('Test 1', 'aa bb cc dd ee', True),
    ('Test 2', 'aa bb cc dd aa', False),
    ('Test 3', 'aa bb cc dd aaa', True),
]

for name, input, expected in grade_sheet:
    solution = solve(input)
    if expected is not solution:
        print('[x] %s failed: got %s' % (name, solution))
    else:
        print('[] %s passed' % name)

import os
fname = os.getcwd() + '/solutions/04/input'
with open(fname) as f:
    input = f.readlines()
input = [x.strip() for x in input]

x = 0
for i in input:
    if solve(i):
        x += 1

print('Solution: %s' % x)
