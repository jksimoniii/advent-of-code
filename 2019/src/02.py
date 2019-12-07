# OPCODES
#  - 1: addition
#  - 2: multiplication
#  - 99: halt


OPCODE_EXEC = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    99: None
}


def intcode_runner(intcode, noun=12, verb=2):
    pos = 0
    intcode[1] = noun
    intcode[2] = verb
    while True:
        opcode = intcode[pos]
        if opcode not in OPCODE_EXEC:
            raise Exception('Unexpected OPCODE: {}'.format(opcode))
        fn = OPCODE_EXEC[opcode]
        if not fn:
            return intcode[0]
        p1, p2, p3 = intcode[pos+1:pos+4]
        intcode[p3] = fn(intcode[p1], intcode[p2])
        pos += 4


def find_output(intcode, desired_output):
    for noun in range(100):
        for verb in range(100):
            try:
                output = intcode_runner(intcode.copy(), noun=noun, verb=verb)
            except Exception as e:
                continue
            if output == desired_output:
                return 100 * noun + verb


if __name__ == '__main__':
    f = open('/data/02.txt')
    intcode = list(map(int, f.readline().split(',')))
    print('Part 1: {}'.format(intcode_runner(intcode.copy())))
    print('Part 2: {}'.format(find_output(intcode.copy(), 19690720)))

