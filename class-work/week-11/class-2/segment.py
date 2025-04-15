from __future__ import annotations
from point2 import Point

class Segment:
    ''' Line Segments '''

    def __init__(self, p1: Point, p2: Point):
        '''Create Segment between P1 and P2'''
        self.p1 = p1
        self.p2 = p2

    def translate(self, dx: int, dy: int) -> None:
        '''Move segment dx horizontally and dy vertically'''
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)

    def length(self) -> float:
        '''Return length of Segment'''
        return self.p1.distance(self.p2)

    def __lt__(self, other_segment) -> bool:
        '''Less-than comparison based on segment length'''
        return isinstance(other_segment, Segment) and self.length() < other_segment.length()

# Example usage
p1 = Point(3, 4)
p2 = Point(0, 0)
line_seg = Segment(p1, p2)
length1 = line_seg.length()
print(f'length1: {length1}')

p3 = Point(2, 3)
p4 = Point(7, 8)
line_seg2 = Segment(p3, p4)
length2 = line_seg2.length()
# print(f'length2: {length2}')

print(f'Segment 1 < Segment 2? {line_seg < line_seg2}')

# Work try to do relational operators and __repr__