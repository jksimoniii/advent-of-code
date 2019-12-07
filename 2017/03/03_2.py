grid = []


class Block(object):
    x_pos = 0
    y_pos = 0
    orientation = 0  # 0-right, 1-up, 2-left, 3-down
    value = 0


def get_block(x, y):
    return list(filter(lambda block: block.x_pos is x and block.y_pos is y, grid))


def block_exists(x, y):
    return len(get_block(x, y)) > 0


def get_neighbors(x, y):
    return [
        get_block(x+1, y),
        get_block(x+1, y+1),
        get_block(x, y+1),
        get_block(x-1, y+1),
        get_block(x-1, y),
        get_block(x-1, y-1),
        get_block(x, y-1),
        get_block(x+1, y-1)
    ]


def calculate_value(x, y):
    neighbors = get_neighbors(x, y)
    value = 0
    for neighbor in neighbors:
        if len(neighbor) < 1:
            continue

        value += neighbor.pop(0).value

    return value


def compute_steps(orientation):
    if orientation is 0:
        steps = (1, 0)
    elif orientation is 1:
        steps = (0, 1)
    elif orientation is 2:
        steps = (-1, 0)
    elif orientation is 3:
        steps = (0, -1)

    return steps
    

def step():
    block = grid[-1]
    if len(grid) is 1:
        block.value = 1
        return block.value

    parent = grid[-2]
    orientation = parent.orientation
    x_step, y_step = compute_steps(orientation)
    x_pos = parent.x_pos + x_step
    y_pos = parent.y_pos + y_step

    while block_exists(x_pos, y_pos):
        orientation = (orientation - 1) % 4
        x_step, y_step = compute_steps(orientation)
        x_pos = parent.x_pos + x_step
        y_pos = parent.y_pos + y_step

    block.orientation = (orientation + 1) % 4
    block.x_pos = x_pos
    block.y_pos = y_pos
    block.value = calculate_value(block.x_pos, block.y_pos)

    return block.value


def solve(input):
    value = 0
    while value <= input:
        grid.append(Block())
        value = step()

    return value



grade_sheet = [
    ('Test 1', 1, 2),
    ('Test 2', 2, 4),
    ('Test 3', 4, 5),
    ('Test 4', 5, 10)
]

for name, input, expected in grade_sheet:
    solution = solve(input)
    if expected is not solution:
        print('[x] %s failed: got %s' % (name, solution))
    else:
        print('[] %s passed' % name)

input = 325489
print('Solution: %s' % solve(input))