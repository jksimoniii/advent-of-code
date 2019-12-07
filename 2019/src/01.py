import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_fuel_requirements(modules, include_fuel=False):
    sum = 0
    for module in modules:
        fuel_mass = calculate_fuel(module)
        sum += fuel_mass
        if include_fuel:
            while fuel_mass > 0:
                fuel_mass = calculate_fuel(fuel_mass)
                if fuel_mass > 0:
                    sum += fuel_mass
    return sum


if __name__ == '__main__':
    f = open('/data/01.txt')
    line = f.readline()
    modules = []
    while line:
        modules.append(int(line.strip()))
        line = f.readline()
    print('Part 1: {}'.format(calculate_fuel_requirements(modules)))
    print('Part 2: {}'.format(calculate_fuel_requirements(modules, include_fuel=True)))

