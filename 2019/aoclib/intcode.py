class IntcodeComputer:
    INSTRUCTIONS = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        99: lambda: IntcodeComputer.halt_execution()
    }
    PARAM_MODE_POSITION = 0
    PARAM_MODE_IMMEDIATE = 1
    pos = 0

    def __init__(self, program):
        self.program = program

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        opcode = self.program[self.pos]
        if opcode not in IntcodeComputer.INSTRUCTIONS:
            raise Exception('Unexpected OPCODE: {}'.format(opcode))
        elif opcode == 99:
            self.halt_execution()
        fn = IntcodeComputer.INSTRUCTIONS.get(opcode)
        p1, p2, p3 = self.program[self.pos+1:self.pos+4]
        self.program[p3] = fn(self.program[p1], self.program[p2])
        self.pos += 4

    def run(self):
        for _ in self:
            pass
        return self.program[0]

    @classmethod
    def halt_execution(cls):
        raise StopIteration

    @classmethod
    def init_from_file(cls, filename):
        with open(filename, 'r') as f:
            program = list(map(int, f.readline().split(',')))
        return cls(program)
