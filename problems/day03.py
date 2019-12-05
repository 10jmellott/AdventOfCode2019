from functools import reduce
from math import floor

def _load_file():
    # Open the file in read-only mode
    return open('data/03.txt', 'r')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x},{self.y}'

class Segment:
    def __init__(self, p, str):
        self.p1 = p
        direction = str[0]
        self.length = int(str.strip()[1:])
        if direction == 'U':
            self.p2 = Point(p.x, p.y + self.length)
        elif direction == 'D':
            self.p2 = Point(p.x, p.y - self.length)
        elif direction == 'R':
            self.p2 = Point(p.x + self.length, p.y)
        elif direction == 'L':
            self.p2 = Point(p.x - self.length, p.y)

    def getIntersection(self, other):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        x3 = other.p1.x
        y3 = other.p1.y
        x4 = other.p2.x
        y4 = other.p2.y

        det = (x4 - x3) * (y1 - y2) - (x1 - x2) * (y4 - y3)

        if det == 0:
            return None
        
        detA = (y3 - y4) * (x1 - x3) + (x4 - x3) * (y1 - y3)
        tA = detA / det

        if tA < 0:
            return None
        if tA > 1:
            return None

        detB = (y1 - y2) * (x1 - x3) + (x2 - x1) * (y1 - y3)
        tB = detB / det

        if tB < 0:
            return None
        if tB > 1:
            return None
        
        return Point(x1 + tA * (x2 - x1), y1 + tA * (y2 - y1))

def _toSegments(f):
    data = list(f.readline().split(','))
    p = Point(0, 0)
    segments = []
    for d in data:
        s = Segment(p, d)
        p = s.p2
        segments.append(s)
    return segments
    
def _part1():
    f = _load_file()
    segments1 = _toSegments(f)
    segments2 = _toSegments(f)
    intersections = []
    for s1 in segments1[1:]:
        for s2 in segments2[1:]:
            intersection = s1.getIntersection(s2)
            if intersection != None:
                intersections.append(intersection)
    minIntersection = min(map(lambda p: abs(p.x) + abs(p.y), intersections))
    return minIntersection

def _part2():
    f = _load_file()
    segments1 = _toSegments(f)
    segments2 = _toSegments(f)

    minIntersection = 10000000

    wire1Length = segments1[0].length
    for s1 in segments1[1:]:
        wire2Length = segments2[0].length
        for s2 in segments2[1:]:
            intersection = s1.getIntersection(s2)
            if intersection != None:
                w1Dist = wire1Length + abs(intersection.x - s1.p1.x) + abs(intersection.y - s1.p1.y)
                w2Dist = wire2Length + abs(intersection.x - s2.p1.x) + abs(intersection.y - s2.p1.y)
                minIntersection = min(minIntersection, w1Dist + w2Dist)
            wire2Length = wire2Length + s2.length
        wire1Length = wire1Length + s1.length
    return minIntersection

def main():
    return _part1(), _part2()

main()
