class Progression:
    ''' 
    Iterator producing a generic progression.
    Default iterator produces the whole numbers.
    '''
    def __init__(self, start=0):
        self._current = start  # this _ means that this should only be used in this class

    def _advance(self):
        '''Update self._current to a new value.'''
        self._current += 1  # current is a pointer

    def __next__(self):
        '''Return the new element, or else raise StopIteration.'''
        answer = self._current
        self._advance()
        return answer

    def printProgression(self, n):
        '''Print the next n values of the progression.'''
        print(' '.join(str(next(self)) for _ in range(n)))  # take the next values in this iterator and change it into a string

    def lstProgression(self, n):
        '''Return the next n values of the progression as a list.'''
        return [next(self) for _ in range(n)]  # returns a list of the next n progression values
    
if __name__ == '__main__':
    print('Default Progression:')
    Progression().printProgression(10)
    Progression().printProgression(12)

    for value in Progression().lstProgression(12):
        print(value)