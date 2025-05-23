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
'''
Topics to study for the exam:
1. Data Science Libraries (short type questions, multiple choice questions)
    -> pandas, matplotlib, numpy DONE
2. Debugging  DONE
    -> 'here's a lil snippet of code, here what i want to output, where do i put the breakpoint'
    -> 'find 5 errors and tell me how to fix it'
3. 2D lists + tuples nested loops DONE
    -> tuple is immutable!!
    -> lst = ['a', 'b', 'c']
       t = (3, 4, lst)
       lst.append('d')
       print(t)
       >>> (3, 4, ['a', 'b', 'c', 'd'])
3.5. List comprehensions, map, filter (trace the code type questions and questions were you're allowed to use)
4. Dictionaries, nested Dictionaries, sets
5. Files, json, exceptions
    -> open('file.txt', 'r')
       open('file.txt', 'w')
    -> with open('file.txt', 'r') as f:
           f.read()
           f.readline()
           f.readlines()
           f.write()
           f.writelines()
    -> json.load
    -> json.dump
    -> try, except, finally
5.5. Stack ADT
    -> LIFO (Last In First Out)
    -> push, pop, peek
    -> stack = []
       stack.append(1)
       stack.append(2)
       stack.append(3)
       print(stack.pop())
       >>> 3
       print(stack)
       >>> [1, 2]
6.  Object-oriented programming
    -> classes
    -> containment (has-a relationship) + annotations
    -> inheritance (is-a relationship)
    -> abstract classes
    -> relational operators + arithmetic operators + total ordering
    -> iterators + iterables (__iter__ and __next__)
    -> encapsulation (private/protected/public attributes and methods)
       -> pandas:
          __var1 -> private
          _var2 -> protected
          var3  -> public
          definition of private: only accessible within the class
          definition of protected: accessible within the class and its subclasses
          definition of public: accessible from anywhere
    -> polymorphism (same functions takes different forms from different classes - method overloading)
7. Recursion
    -> base case
    -> recursive case
    -> stack overflow
    -> tail recursion
8. Sorting/searching:
    -> selction sort O(n^2)
    -> insertion sort O(n^2)
    -> merge sort O(nlogn)
    -> quick sort O(nlogn) -> O(n^2) worst case
    -> binary search O(logn)
    -> bisect module

Potential content: like 2 exams combined
- 4 long answer questions
- a shit-ton of multiple choice questions
- tracing code questions
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

#for val in FibonacciIterable(10):
#    print(val)

class PowerOfThreeIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return PowerOfThreeSequence(self.n)
    
    def as_list(self):
        return [val for val in self]
    
class PowerOfThreeSequence:
    def __init__(self, n):
        self.end = n
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.end:
            raise StopIteration
        else:
            result = 3 ** self.count
            self.count += 1
            return result

#for val in PowerOfThreeIterable(5):
#    print(val)
#print(PowerOfThreeIterable(5).as_list())

class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        answer = self._current
        self._advance()
        return answer

    def __iter__(self):
        return self

    def printProgression(self, n):
        print(' '.join(str(next(self)) for _ in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self.increment = increment

    def _advance(self):
        self._current += self.increment

class SquareRootProgression(Progression):
    def __init__(self, start=1):
        super().__init__(start)

    def _advance(self):
        self._current = self._current ** 0.5

class AlternatingProgression(Progression):
    def __init__(self, start=0):
        super().__init__(start)
        self._initial = start
        self._sign = 1

    def _advance(self):
        self._initial += 1
        self._sign *= -1
        self._current = self._initial * self._sign


# if __name__ == '__main__':
#     a = ArithmeticProgression(increment=5, start=2)
#     a.printProgression(8)
#     a = SquareRootProgression(start=144)
#     a.printProgression(4)
#     a = AlternatingProgression(start=1)
#     a.printProgression(10)

class TimerTick:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        answer = self._current
        self._advance()
        return answer
    
    def showTicks(self, n):
        print(' '.join(str(next(self)) for _ in range(n)))

class ConstantTimer(TimerTick):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self.increment = increment
    
    def _advance(self):
        self._current += self.increment

class DoublingTimer(TimerTick):
    def __init__(self, start=0):
        super().__init__(start)
    
    def _advance(self):
        self._current *= 2

class OddTimer(TimerTick):
    def __init__(self, start=0):
        super().__init__(start)
    
    def _advance(self):
        self._current += 2

# print("Constant Timer:")
# ConstantTimer(3, 0).showTicks(5)
# # 0 3 6 9 12

# print("Doubling Timer:")
# DoublingTimer(1).showTicks(6)
# # 1 2 4 8 16 32

# print("Odd Timer:")
# OddTimer(start=1).showTicks(6)
# # 1 3 5 7 9 11

class FactorialProgression:
    def __init__(self, start):
        self.current = start

    def _advance(self):
        self.current += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        result_i = self.current
        result_f = 1
        for i in range(result_i):
            result_f *= (i+1)
        self._advance()
        return result_f
    
    def printProgression(self, n):
        print(' '.join(str(next(self)) for _ in range(n)))

class DoubleFactorialProgression(FactorialProgression):
    def __init__(self, start=0):
        super().__init__(start)

    def __next__(self):
        result = 1
        n = self.current
        while n > 0:
            result *= n
            n -= 2
        self._advance()
        return result

# FactorialProgression(1).printProgression(5)
# DoubleFactorialProgression(1).printProgression(5)

# inheritance (is-a relationship)

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f'This is a shape called {self.name}'
    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# r = Rectangle("MyRectangle", 4, 5)
# print(r.describe())       # This is a shape called MyRectangle
# print(r.area())           # 20
# print(r.perimeter())      # 18

from abc import ABCMeta, abstractmethod

class Animal(object, metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return 'Woof!'
    
class Cat(Animal):
    def make_sound(self):
        return 'Meow!'

class Cow(Animal):
    def make_sound(self):
        return 'Moo!'

animals = [
    Dog("Rex"),
    Cat("Luna"),
    Cow("Daisy"),
]

# for animal in animals:
#     print(f"{animal.name} says {animal.make_sound()}")

class Vehicle(object, metaclass = ABCMeta):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, num_doors=4):
        super().__init__(brand, model)
        self.doors = num_doors

    def start_engine(self):
        print("Car Engine Started")

    def get_info(self):
        return f'Brand: {self.brand}\nModel: {self.model}\n\
Doors: {self.doors}'
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, sidecar):
        super().__init__(brand, model)
        self.sidecar = sidecar

    def start_engine(self):
        print("Car Engine Started")
    
    def get_info(self):
        return f'Brand: {self.brand}\nModel: {self.model}\n\
Sidecar?: {self.sidecar}'
    
# Create a car
car = Car("Toyota", "Camry", 4)
#car.start_engine()           # Output: Car engine started
#print(car.get_info())        # Output: Brand: Toyota, Model: Camry, Doors: 4

# Create a motorcycle
bike = Motorcycle("Harley-Davidson", "Street 750", False)
#bike.start_engine()          # Output: Motorcycle engine started
#print(bike.get_info())       # Output: Brand: Harley-Davidson, Model: Street 750, Has Sidecar: No

# OOP: iterating over objects, nested objects, doctests 

class Range:
    def __init__(self, start, end, increment=1):
        self.start = start
        self.end = end
        self.increment = increment
    
    def __iter__(self):
        return RangeIterator(self.start, self.end, self.increment)
    
class RangeIterator:
    def __init__(self, start, end, increment):
        self.start = start
        self.end = end
        self.increment = increment

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            current = self.start
            self.start += self.increment
            return current
    
elem = Range(1, 10, 3)
# for i in elem:
#     print(i)
'''
7. Recursion
    -> base case
    -> recursive case
    -> stack overflow
    -> tail recursion
8. Sorting/searching:
    -> selction sort O(n^2)
    -> insertion sort O(n^2)
    -> merge sort O(nlogn)
    -> quick sort O(nlogn) -> O(n^2) worst case
    -> binary search O(logn)
    -> bisect module
'''
def recursive_sum(num):
    if num == 0:
        return 0
    else:
        return num + recursive_sum(num - 1)

recursive_sum(5)

def is_palindrome(s):
    s = s.replace(' ', '').lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# print(is_palindrome("racecar"))         # True
# print(is_palindrome("RaceCar"))         # True
# print(is_palindrome("taco cat"))        # True
# print(is_palindrome("python"))          # False
# print(is_palindrome("A man a plan a canal Panama"))  # True

def reverse_string(s):
    s = s.lower()
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

# print(reverse_string("hello"))         # "olleh"
# print(reverse_string("race car"))       # "racecar"
# print(reverse_string("python"))        # "nohtyp"

def count_elements(lst):
    if not lst:
        return 0

    first = lst[0]
    rest = lst[1:]

    if isinstance(first, int):
        return 1 + count_elements(rest)
    elif isinstance(first, list):
        return count_elements(first) + count_elements(rest)
    else:
        return count_elements(rest)

# print(count_elements([1, 2, [3, 4], [5, [6, 7]]]))  # → 7
# print(count_elements([[], [[], [1, 2, [3]]]]))      # → 3
# print(count_elements([]))                           # → 0

def nested_sum(lst):
    if not lst:
        return 0
    
    first = lst[0]
    rest = lst[1:]

    if isinstance(first, int):
        return first + nested_sum(rest)
    elif isinstance(first, list):
        return nested_sum(first) + nested_sum(rest)
    else:
        return nested_sum(rest)

# print(nested_sum([1, 2, 3]))                    # 6
# print(nested_sum([1, [2, 3], 4]))              # 10
# print(nested_sum([[1, 2], [3, [4]], 5]))       # 15
# print(nested_sum([[[[1]]], 2, [[3]]]))         # 6
# print(nested_sum([]))                          # 0
    
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
# Example:
# print(selection_sort([5, 2, 8, 1, 3]))  # [1, 2, 3, 5, 8]

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = mergeSort(left_half) # 'sorted' means its only 1 element
    sorted_right = mergeSort(right_half)

    return sorted_right, sorted_left

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list
    
def insertion_sort2(lst):
    for i in range(1, len(lst)):
        value_to_sort = lst[i]
        while lst[i-1] > value_to_sort and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i - 1
    return lst

arr = [12, 11, 13, 5, 6]
#print(insertion_sort2(arr))

def insertionSort(arr):
    for i in range(1, len(arr)):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
 
arr = [12, 11, 13, 5, 6, 34, 4, 25, 3]
insertionSort(arr)
#print(arr)

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

#arr = [2, 6, 5, 1, 7, 4, 3]
#print(quick_sort(arr))

"""
Deterministic Quicksort:
1. find pivot & partition O(n)
2. recursively sort left O(1) # function call itself is constant
3. recursivelly sort right O(1)

[1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
    <       [ ]         >

Best case scenario: O(nlogn)
                [n]                 O(n)
               /   \
          ~[n/2]    ~[n/2]          O(n)
          /   \      /    \
     ~[n/4] ~[n/4] ~[n/4] ~[n/4]    O(n)

Height of the tree: O(logn)

Worst case scenario: O(n^2)
                [n]                 O(n)
               /   \
          ~[n-1]    ~[0]            O(n)
          /   \      /   \
     ~[n-2] ~[0]  ~[0]  ~[0]        O(n)

Height of the tree: O(n)
"""

# Iterative Binary Search
def binarySearch1(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

# Recursive Binary Search
def binarySearch2(lst, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return binarySearch2(lst, mid + 1, high, target)
        else:
            return binarySearch2(lst, low, mid - 1, target)
    return -1

# # Test
# lst = [2, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 20]
# elem = 5
# print(binarySearch1(lst, elem))                      # Output: 2
# print(binarySearch2(lst, 0, len(lst) - 1, elem))     # Output: 2

# import bisect

# lst = [1, 3, 4, 4, 4, 6, 7]

# # using bisect() to find index to insert new element
# # returns 5 ( right most possible index )
# print ("Rightmost index to insert, so list remains sorted is : ",
#        end="")
# print (bisect.bisect(lst, 4))

# # using bisect_left() to find index to insert new element
# # returns 2 ( left most possible index )
# print ("Leftmost index to insert, so list remains sorted is : ", 
#        end="")
# print (bisect.bisect_left(lst, 4))

# # using bisect_right() to find index to insert new element
# # returns 4 ( right most possible index )
# print ("Rightmost index to insert, so list remains sorted is : ",
#        end="")
# print (bisect.bisect_right(lst, 4, 0, 4))

def sum_matrix(matrix):
    value = 0
    for lst in matrix:
        value += sum(lst)
    return value

#print(sum_matrix([[1, 2], [4, 5], [3, 6]]))

def transpose(matrix):
    lst1 = []
    for i in range(len(matrix[0])):
        lst2 = []
        for j in range(len(matrix)):
            lst2.append(matrix[j][i])
        lst1.append(lst2)
    return lst1

#print(transpose([[1, 2, 3], [4, 5, 6]]))
# Output: [[1, 4], [2, 5], [3, 6]]

#print([[i*j for i in range(1, 6)] for j in range(1, 6)])

def search(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if target == matrix[i][j]:
                return True
    return False

#print(search([[1, 2], [4, 5], [3, 6]], 7))

# Q5 a. O(n^2) b. O(n) c. O(log n)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#print(factorial(5))

def sum_matrix2(matrix):
    if len(matrix) == 1:
        return sum(matrix[0])
    value = sum(matrix[0])
    return value + sum_matrix2(matrix[1:])

#print(sum_matrix2([[1, 2], [4, 5], [3, 6]])) # 21

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

#print(fib(100)) # 21

def flatten_and_sum(matrix):
    if not matrix:
        return [], 0  # base case: empty list

    first = matrix[0]
    rest = matrix[1:]

    # Recursively flatten and sum the rest
    flat_rest, sum_rest = flatten_and_sum(rest)

    if isinstance(first, int):
        return [first] + flat_rest, first + sum_rest
    elif isinstance(first, list):
        flat_first, sum_first = flatten_and_sum(first)
        return flat_first + flat_rest, sum_first + sum_rest
    else:
        return flat_rest, sum_rest

    
#print(flatten_and_sum([1, 2, [3, 4], [5, [6, 7]]]))

def tuples(lst):
    grades_sum = 0
    student = lst[0]
    for i in range(len(lst)):
        grades_sum += lst[i][1]
        if student[1] < lst[i][1]:
            student = lst[i]
    return student[0], grades_sum//len(lst)
    
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 90)]
#print(tuples(students))

def nested_dct(d):
    average_d = {}
    for key in d:
        grades = d[key]['grades']
        avg = sum(grades) // len(grades)
        average_d[key] = avg
    return average_d

students = {
    "Alice": {"age": 20, "grades": [85, 90, 82]},
    "Bob": {"age": 22, "grades": [78, 75, 80]}
}
#print(nested_dct(students))

s1 = {'fig', 'apricot', 'plum', 'peach'}
s2 = {'cherry', 'plum', 'peach'}
s3 = {'raspberry', 'blackberry', 'blueberry'}
s2.union(s1)
s2.update(s3)
s3.add('mulberry')
s2.union(s1)
print(s2)

