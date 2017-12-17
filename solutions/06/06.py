import math


def capture_configuration(banks):
    return [str(i) for i in banks]


def find_largest_bank_index(banks):
    m = max(banks)
    indices = [i for i, j in enumerate(banks) if j == m]

    return min(indices)


def step(banks):
    largest_bank_index = find_largest_bank_index(banks)
    blocks_to_redistribute = banks[largest_bank_index]
    distribution = math.floor(blocks_to_redistribute / (len(banks) - 1))
    remainder = blocks_to_redistribute - (distribution * (len(banks) - 1))
    banks[largest_bank_index] = 0
    for i, bank in enumerate(banks):
        if i is largest_bank_index:
            continue

        banks[i] += distribution

    if distribution > 0:
        banks[largest_bank_index] = remainder
    else:
        i = (largest_bank_index + 1) % len(banks)
        while remainder > 0:
            banks[i] += 1
            remainder -= 1
            i = (i+1) % len(banks)

    return banks


def solve(input):
    banks = list(map(lambda x: int(x), input.split('   ')))
    seen_configurations = []
    config = capture_configuration(banks)
    steps = 0
    while config not in seen_configurations:
        seen_configurations.append(config)
        banks = step(banks)
        config = capture_configuration(banks)
        steps += 1

    return steps


grade_sheet = [
    ('Test 1', '0   2   7   0', 5),
]

for name, input, expected in grade_sheet:
    solution = solve(input)
    if expected is not solution:
        print('[x] %s failed: got %s' % (name, solution))
    else:
        print('[] %s passed' % name)

input = '11   11   13   7   0   15   5   5   4   4   1   1   7   1   15   11'
print('Solution: %s' % solve(input))