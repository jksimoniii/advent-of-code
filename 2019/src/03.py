# coord = (x, y)
# Instructions:
#   R: Right (+x, y)
#   U: Up (x, +y)
#   L: Left (-x, y)
#   D: Down (x, -y)

INSTRUCTIONS_FN = {
    'R': lambda x, y: (x+1, y),
    'U': lambda x, y: (x, y+1),
    'L': lambda x, y: (x-1, y),
    'D': lambda x, y: (x, y-1),
}


def manhattan_distance(p2, p1=(0, 0)):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def instructions_to_coords(instructions, include_steps=False):
    coords = []
    x = 0
    y = 0
    steps = 0
    for i in instructions:
        fn = INSTRUCTIONS_FN.get(i[0])
        for _ in range(int(i[1:])):
            steps += 1
            x, y = fn(x, y)
            if include_steps:
                coords.append((x, y, steps))
            else:
                coords.append((x, y))
    return coords


if __name__ == '__main__':
    with open('data/03.txt') as f:
        wires = [l.strip().split(',') for l in f.readlines()]
    coords = list(map(instructions_to_coords, wires))
    intersections = set(coords[0]) & set(coords[1])
    print('Part 1: {}'.format(min(map(manhattan_distance, intersections))))
    print('Part 2: {}'.format(min([list(coords[0]).index(i) + list(coords[1]).index(i) + 2 for i in intersections])))

