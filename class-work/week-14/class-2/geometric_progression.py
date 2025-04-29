from progression import Progression  # Assuming the Progression class is in a separate file.

class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)  # Call the parent constructor with the starting value.
        self._base = base  # The base multiplier for the geometric progression.

    def _advance(self):
        '''Update self._current by multiplying it by the base.'''
        self._current *= self._base  # Multiply the current value by the base.

if __name__ == '__main__':
    print('Geometric Progression (Base 2):')
    p = GeometricProgression(base=2, start=1)  # Start at 1, with a base of 2.
    p.printProgression(10)  # Print the first 10 terms of the geometric progression.
    
    print('Geometric Progression (Base 3):')
    p2 = GeometricProgression(base=3, start=1)  # Start at 1, with a base of 3.
    p2.printProgression(10)  # Print the first 10 terms of the geometric progression.
