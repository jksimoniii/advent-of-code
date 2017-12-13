import math

def calc_box_height(input):
    x = 1
    while x**2 < input:
        x += 2

    return x


# 0 is the bottom, move clockwise
def calc_box_side(box_height, input):
    for i in range(4):
        max = (box_height**2)-(box_height*i) + i + 1
        min = max - box_height
        if i is 3:
            min += 1
        row = range(min, max)
        if input in row:
            return list(row) if i % 2 is 0 else list(reversed(row))


def solve(input):
    box_height = calc_box_height(input)
    box_side = calc_box_side(box_height, input)
    if box_side is None:
        return 0

    d_center = math.floor(box_height/2)
    pos = box_side.index(input)
    d_axis = abs(d_center - pos)
    return d_axis + d_center

grade_sheet = [
    ('Test 1', 1, 0),
    ('Test 2', 12, 3),
    ('Test 3', 23, 2),
    ('Test 4', 1024, 31)
]

for name, input, expected in grade_sheet:
    solution = solve(input)
    if expected is not solution:
        print('[x] %s failed: got %s' % (name, solution))
    else:
        print('[] %s passed' % name)

input = 325489
print('Solution: %s' % solve(input))