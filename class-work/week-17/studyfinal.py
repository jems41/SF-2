'''
Week 1: Recap on SF-1
Week 2-3: Data Science Libraries: pandas, matplotlib, numpy
Week 3-4: Debugging
Week 4-5: 2D lists, list comprehension, matrix
Week 6, 15: Big O and recursion
Week 6-7: Dictionaries
Week 8: Sets
Week 9-10: Read/Write files & exceptions
Week 11-13: OOP: objects, constructors, inheritance hierarchy, polymorphism
Week 14: OOP: iterating over objects, nested objects, doctests
Week 15-16: Sorting and Searching Algorithms

Today: Week 13-16
Tomorrow: Week 1-8
Thursday: Week 9-12
'''

# OOP: iterating over objects, nested objects, doctests

class EvenNumbers:
    def __init__(self, end):
        self._end = end
        self._count = 0
        self._current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._count >= self._end:
            raise StopIteration
        answer = self._current
        self._current += 2
        self._count += 1
        return answer
    
    def reset(self):
        reset = self._end
        return reset
    
if __name__ == '__main__':
    even = EvenNumbers(5)

    #for number in even:
    #    print(f'Even:{number}')

class OddNumbers:
    def __init__(self, end):
        self._end = end
        self._count = 0
        self._result = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._count >= self._end:
            raise StopIteration
        else:
            result_i = self._result
            self._result += 2
            self._count += 1
        return result_i
    
    def reset(self):
        reset = self._end
        return reset
    
if __name__ == '__main__':
    even = OddNumbers(5)

    #for number in even:
    #    print(f'Odd:{number}')

class SquareIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return SquareSequence(self.n)
    
class SquareSequence:
    def __init__(self, n):
        self.end = n
        self.count = 0
        self.result = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.end:
            raise StopIteration
        else:
            self.count += 1
            result = self.count ** 2
            return result
        
#for val in SquareIterable(5):
    #print(val)

class FibonacciIterable: # homework
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return FibonacciSequence(self.n)

class FibonacciSequence:
    def __init__(self, n):
        self.num = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.num:
            raise StopIteration
        else:
            a_i = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return a_i

for val in FibonacciIterable(10):
    print(val)