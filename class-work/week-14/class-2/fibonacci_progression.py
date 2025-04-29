from progression import Progression

class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first  # This is used to keep track of the previous term.

    def _advance(self):
        '''Update the current term by adding the previous two terms.'''
        self._current, self._prev = self._current + self._prev, self._current  # Update current and previous terms.

if __name__ == '__main__':
    print('Fibonacci Progression:')
    p = FibonacciProgression(first=0, second=1)  # Start with 0 and 1 as the first two terms.
    p.printProgression(10)  # Print the first 10 terms of the Fibonacci progression.

