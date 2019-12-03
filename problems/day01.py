from functools import reduce
from math import floor

def _load_file():
    # Open the file in read-only mode
    return open('data/01.txt', 'r')

def _getFuel(mass):
    
    return floor(mass / 3.0) - 2

def _getTotalFuel(mass):
    if mass < 9:
        return 0
    partial = _getFuel(mass)
    return partial + _getTotalFuel(partial)

def _part1():
    f = _load_file()
    return reduce(lambda x, y: x + y, map(lambda l: _getFuel(int(l)), f))

def _part2():
    f = _load_file()
    return reduce(lambda x, y: x + y, map(lambda l: _getTotalFuel(int(l)), f))

def main():
    return _part1(), _part2()
