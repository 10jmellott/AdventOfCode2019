from functools import reduce
from math import floor

def _isPotentialPassword(password, preventTriples):
    hasDouble = False
    value = 0
    for i in range(5):
        if password[i] > password[i + 1]:
            return False
        if not hasDouble and password[i] == password[i + 1]:
            if preventTriples:
                if i > 0 and password[i - 1] == password[i]:
                    hasDouble = False
                elif i < 4 and password[i] == password[i + 2]:
                    hasDouble = False
                else:
                    hasDouble = True
            else:
                hasDouble = True
        value = value * 10 + password[i]
    
    if not hasDouble:
        return False

    value = value * 10 + password[5]

    if value < 234208:
        return False
    if value > 765869:
        return False
    
    return True

    

def _part1():
    count = 0
    for i0 in range(10):
        for i1 in range(10):
            for i2 in range(10):
                for i3 in range(10):
                    for i4 in range(10):
                        for i5 in range(10):
                            if _isPotentialPassword([i0, i1, i2, i3, i4, i5], False):
                                count = count + 1
    return count


def _part2():
    count = 0
    for i0 in range(10):
        for i1 in range(10):
            for i2 in range(10):
                for i3 in range(10):
                    for i4 in range(10):
                        for i5 in range(10):
                            if _isPotentialPassword([i0, i1, i2, i3, i4, i5], True):
                                count = count + 1
    return count

def main():
    return _part1(), _part2()

_part1()
