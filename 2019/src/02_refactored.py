from aoclib.intcode import IntcodeComputer


def find_output(desired_output):
    for noun in range(100):
        for verb in range(100):
            try:
                computer = IntcodeComputer.init_from_file('/data/02.txt')
                computer.program[1] = noun
                computer.program[2] = verb
                output = computer.run()
            except Exception as e:
                continue
            if output == desired_output:
                return 100 * noun + verb


if __name__ == '__main__':
    f = open('/data/02.txt')
    intcode = list(map(int, f.readline().split(',')))
    computer = IntcodeComputer.init_from_file('/data/02.txt')
    computer.program[1] = 12
    computer.program[2] = 2
    print('Part 1: {}'.format(computer.run()))
    print('Part 2: {}'.format(find_output(19690720)))

