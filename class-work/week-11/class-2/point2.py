from __future__ import annotations # to fix Point not getting recognized
import math

class Point: # always takes the latest one
    # def __init__(self):
    #     '''
    #     Create a two-dimensional point at (0, 0)
    #     '''
    #     self.x = 0
    #     self.y = 0

    def __init__(self, x: int, y: int): # it's now a user input
        '''
        Create two-dimensional Point at (x, y)
        '''
        self.x = x
        self.y = y

    def translate(self, dx: int, dy: int):
        '''
        Move point dx horizontally and dy vertically
        '''
        self.x += dx
        self.y += dy

    def distance(self, other_point: Point) -> float:
        '''
        Return the distance between this (i.e. self) Point
        and other point
        '''
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2
        return math.sqrt(a + b)
    
    def __repr__(self) -> str:
        '''
        return x, y coordinates of Point (x, y)
        '''
        return f'({self.x}, {self.y})'
        
    def __lt__(self, other_point: Point) -> bool:
        '''
        return True if this Point and other_point are of
        type Point and x, y coordinates of this Point are <
        x, y coordinates of other_point
        '''
        return isinstance(other_point, Point) and \
                self.x < other_point.x and self.y < other_point.y
    
    def __eq__(self, other_point: Point) -> bool:
        return isinstance(other_point, Point) and \
                self.x == other_point.x and self.y == other_point.y

###################
# Main Program

p1 = Point(0, 0)
print(f'(x, y) coordinates of p1: ({p1.x}, {p1.y})')

p1.translate(4, 2)
print(f'(x, y) coordinates of p1: ({p1.x}, {p1.y})') # new coords

p2 = Point(4, 3)
print(p1.distance(p2)) # take distance from p1 to p2 

print(f'p1 <? p2: {p1 < p2}')
print(f'p1 ==? p2: {p1 == p2}')

