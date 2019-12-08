def length_rule(password):
    return len(str(password)) == 6


def range_rule(password):
    with open('data/04.txt') as f:
        puzzle_input = f.readline()
    min, max = puzzle_input.split('-')
    return int(min) < password < int(max)


def adjacent_rule(password):
    last_seen = None
    for x in str(password):
        if x == last_seen:
            return True
        last_seen = x
    return False


def decrease_rule(password):
    last_seen = None
    for x in str(password):
        if last_seen and int(x) < int(last_seen):
            return False
        last_seen = x
    return True


def modified_adjacent_rule(password):
    password = str(password)
    for x in set(password):
        if password.count(x) == 2:
            return True
    return False


def password_validator(value, rules=[]):
    for rule in rules:
        if not rule(value):
            return False
    return True


def run_validation(additional_rules=[]):
    rules = [length_rule, range_rule, adjacent_rule, decrease_rule]
    with open('data/04.txt') as f:
        puzzle_input = f.readline()
    min, max = puzzle_input.split('-')
    r = range(int(min)+1, int(max))
    valid_passwords = []
    for i in r:
        if password_validator(i, rules=rules+additional_rules):
            valid_passwords.append(i)
    return valid_passwords


if __name__ == '__main__':
    print('Part 1: {}'.format(len(run_validation())))
    print('Part 2: {}'.format(len(run_validation(additional_rules=[modified_adjacent_rule]))))

