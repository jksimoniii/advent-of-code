from functools import reduce


def is_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


class Passphrase(object):
    def __init__(self, value):
        self.value = value
        self.words = self.value.split(' ')

    def is_valid(self):
        for i, word in enumerate(self.words):
            new_words = self.words.copy()
            new_words.pop(i)
            for w in new_words:
                if is_anagram(word, w):
                    return False

        return True


def solve(input):
    passphrase = Passphrase(input)
    return passphrase.is_valid()


grade_sheet = [
    ('Test 1', 'abcde fghij', True),
    ('Test 2', 'abcde xyz ecdab', False),
    ('Test 3', 'a ab abc abd abf abj', True),
    ('Test 4', 'iiii oiii ooii oooi oooo', True),
    ('Test 5', 'oiii ioii iioi iiio', False)
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
