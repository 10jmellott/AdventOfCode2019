from functools import reduce
from math import floor

def _load_file():
    # Open the file in read-only mode
    return open('data/02.txt', 'r')

def _executeIntcode(data, i1, i2):
    data[1] = i1
    data[2] = i2
    i = 0
    opcode = -1
    while opcode != 99 and i < len(data) - 1:
        opcode = data[i]
        if opcode != 99 and i < len(data) - 4:
            pos_input_1 = data[i + 1]
            pos_input_2 = data[i + 2]
            pos_output = data[i + 3]
            output = data[pos_output]
            if opcode == 1:
                output = data[pos_input_1] + data[pos_input_2]
            elif opcode == 2:
                output = data[pos_input_1] * data[pos_input_2]
            data[pos_output] = output 
        i = i + 4
    return data[0]

def _part1():
    f = _load_file()
    data = list(map(lambda l: int(l), f.read().split(',')))
    return _executeIntcode(data, 0, 1)

def _part2():
    f = _load_file()
    sp = f.read().split(',')
    for i1 in range(100):
        for i2 in range(100):
            data = list(map(lambda l: int(l), sp))
            ei = _executeIntcode(data, i1, i2)
            if ei == 19690720:
                return i1 * 100 + i2

def main():
    return _part1(), _part2()
