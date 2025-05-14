'''
Topics to study for the exam:
1. Data Science Libraries (short type questions, multiple choice questions)
    -> pandas, matplotlib, numpy
2. Debugging 
    -> 'here's a lil snippet of code, here what i want to output, where do i put the breakpoint'
    -> 'find 5 errors and tell me how to fix it'
3. 2D lists + tuples nested loops
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