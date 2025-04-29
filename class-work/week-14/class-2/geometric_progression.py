from progression import Progression

class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        '''Update self._current by multiplying it by the base.'''
        self._current *= self._base

if __name__ == '__main__':
    print('Geometric Progression (Base 2):')
    p = GeometricProgression(base=2, start=1)
    p.printProgression(10)
