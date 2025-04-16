'''
To study:
- map() function
- Dictionaries & Sets: week-6 to week-8 (sets: week-8) # somewhat done
    - creating dictionaries and sets
    - iterating through sets and dictionaries
    - dictionary operations, comparisons
    - comparing sets and set theoretic operations
    - mutable set operators and methods
    - nested dictionaries
    - dictionary and set comprehensions
- Read/Write files & exceptions: week-9 to week-10 # HELP IM GOING TO CRASH OUT
    - standard files objects
    - text file processing: reading/writing/updating
    - remove/rename files
    - serialization with JSON
    - handling exceptions
    - try/except/else clause
- Object-Oriented Programming week-11 to week-12 # help me god
    - introducing objects and classes
    - constructors
    - encapsulation
    - differences between is-a and has-a relationships
'''
# dictionnary = a collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {'USA': 'Washington D.C.',
            'India': 'New Delhi', 
            'China': 'Beijing', 
            'Russia': 'Moscow'}

print(capitals.get('Japan')) # None

if capitals.get("China"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()
print(capitals.values())
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

print(capitals)

print('\n \n \n') #---------------------------------------------------------------------------------------#

def combine(d1, d2):
    '''
    return dictionnary where each key is a
    key in both d1 and d2
    the value associated with each key in 
    the new dictionnary is the sum of all the integers
    associated with that key
    in d1 and d2
    '''
    new_dict = {}
    for key in d1:
        if key in d2:
            new_dict[key] = sum(d1[key]) + sum(d2[key])
    return new_dict

d1 = {1: [2], 4: [5, 6]}
d2 = {4: [8]}

print(combine(d1, d2))

print('\n \n \n') #---------------------------------------------------------------------------------------#

def combine2(d1, d2):
    '''
    return dictionnary where each key is a key that is
    a key in the values of d1 and d2.
    The value associated with each key in the the new
    dictionnary is the sum of all the integers associated
    with that key in d1 and d2

    >>> combine2({'a': {3: [2], 4: [5, 6]}, {'a': {3: [8, 12]})
    {3: 22}
    '''
    result = {}
    for key in d1: # iterate through the keys of d1
        if key in d2:
            for k in d1[key]: # iterate through the keys of d1[key] nested dictionnary
                if k in d2[key]:
                    result[k] = sum(d1[key][k]) + sum(d2[key][k])
    return result
                
print(combine2({'a': {3: [2], 4: [5, 6]}}, {'a': {3: [8, 12]}}))

print('\n \n \n') #---------------------------------------------------------------------------------------# LAB-7 (Dictionnaries)

'''
Question1:

Given a dictionary of keys that are strings and/or integers, 
values are lists, write a snippet of code that returns the total number
of elements of all lists that have keys as strings.  
'''

dict = {'apples': [1, 2], 41: [2, 3], 'pears': [4, 5], 'bananas': [6, 7]}

def elemStr(d):
    elem = 0
    for key in d:
        if type(key) == str:
            elem += len(d[key])
    return elem

print(elemStr(dict))

print('\n \n \n') #---------------------------------------------------------------------------------------#
'''
Question2:

Write a function wordTally that takes an integer argument 
n and reads n words from the user.  Note that the user
may enter the same word multiple times.  
Your function should tally up how many times each word
occurs that the user has entered and store it in a dictionary
where the keys are the words and the values are the number
of times each word occurs.  
Return this dictionary. 

You may only create one collection: one dictionary
'''
def wordTally(lst):
    dct = {}
    for key in lst:
        if key in dct:
            dct[key] = dct[key] + 1    
        else:
            dct[key] = 1
    return dct
print(wordTally(['balls', 'balls', 'apple']))

print('\n \n \n') #---------------------------------------------------------------------------------------#
'''
Quesiton3: 

write a function called invertDictionary that takes a 
dictionary d as an argument.  This function inverts the
provided dictionary.  That is, the keys become the values
(as lists) and the values become the keys. 

Note that d may have repetitive values, in which case in 
the inverted dictionary only one of these values
will be used as a key. For such a key, in the inverted
dictionary the value is a list of all such possible
keys from d

For example: 
d = {3: 5, 4: 5, 6: 1}
d_inverted = {5: [3, 4], 1: [6]}
'''
def invertDictionary(d):
    invert_d = {}
    for key in d:
        if d[key] in invert_d:
            invert_d[d[key]] += [key]
        else:
            invert_d[d[key]] = [key]
    return invert_d

d = {3: 5, 4: 5, 6: 1}
print(invertDictionary(d))

print('\n \n \n') #---------------------------------------------------------------------------------------#

'''
Question 4:

Given a sequence of m words and an integer k, find the
k-th most common words.  A word w is the k-th most 
common if exactly k-1 distinct words occur more
frequently than w. 
'''
def common(lst, k):
    dct = {}
    for elem in lst:
        if elem in dct:
            dct[elem] += 1
        else:
            dct[elem] = 1
    sort_d = sorted(dct)
    return sort_d[k-1]

print(common(['balls', 'balls', 'apple', 'apple', 'apple', 'banana'], 2))

print('\n \n \n') #---------------------------------------------------------------------------------------# LAB-8 (Sets)
'''
create a file birthdays.py that will do the following:

(a) write a function that reads birthdays of people
    from the user and stores them in a dictionary
    of dictionaries.  Once the user enters 'stop', you 
    will read no more input from the user.  You may
    assume the user will give valid input.

    Sample Input:
    month day name: February 23 Bob
    month day name: May 3 Katie
    month day name: May 8 Paul
    month day name: May 8 Lucy
    month day name: stop

    Sample Output (i.e. returned by function)
    { 'February': {'23': ['Bob']},
      'May': {'3': ['Katie'], '8': ['Paul', 'Lucy']}
      }
'''
def birthdays():
    user_input = ""
    lst = []
    while user_input != ['stop']:
        user_input = input('month day name ').split()
        if user_input != ['stop']:
            lst.append(user_input)

    birthdays = {}

    for elem in lst:
        if elem[0] not in birthdays:
            birthdays[elem[0]] = {}
        
        if elem[1] not in birthdays[elem[0]]:
            birthdays[elem[0]][elem[1]] = []
        
        birthdays[elem[0]][elem[1]].append(elem[2])

    return birthdays

print('\n \n \n') #---------------------------------------------------------------------------------------#

'''
(b) Write a function called mostCovered that will take 
the dictionary entered by the user in part (a) and
return the month that has the most number of 
birthdays
'''
def mostCovered(): # [[april, 1, james], [april, 1, elliot], [may, 1, martin], [april, 4, joe]]
    # {'april':  {'1': ['james', 'elliot'], '4': ['joe']}, 'may': {'1': ['martin']}}
    dct = birthdays()
    max_count = 0
    max_month = None
    for key in dct:
        count = 0
        for day in dct[key]:
            count += len(dct[key][day])
        if count > max_count:
            max_count = count
            max_month = key
    return max_month

print('\n \n \n') #---------------------------------------------------------------------------------------#

'''
(c) write a function called invert() that will take
the birthday month dictionary entered by the user in
part(a) and return the equivalent brithday dictionary

Sample Input is the dictionary returned in part (a)

Sample Output:
{'Bob': ('February', '23'), 
'Katie': ('May', '3'),
'Paul': ('May', '8'), 
'Lucy': ('May', '8')}
'''
def invert(): # {'april':  {'1': ['james', 'elliot'], '4': ['joe']}, 'may': {'1': ['martin']}}
    dct = birthdays()
    dct_birthday = {}
    for key in dct:
        for day in dct[key]:
            for name in dct[key][day]:
                dct_birthday.update({name: (key, day)}) 
    return dct_birthday

# print(invert())

print('\n \n \n') #---------------------------------------------------------------------------------------#

'''
1. Find the number of mutual friends between Alice and Bob.
2. Find all the friends that are only Alice's (not Bob's)
3. Find all the friends either of them has (no repeats)
4. Check if Bob has any friends Alice doesn't have. (Print True or False)

INPUT:
alice_friends = {"Sam", "Emma", "John", "Alice", "Zara"}
bob_friends = {"John", "Zara", "Lucas", "Mia"}

OUTPUT:
Mutual friends: {'John', 'Zara'}
Only Alice's friends: {'Sam', 'Emma', 'Alice'}
All friends: {'Emma', 'Sam', 'Lucas', 'Alice', 'Mia', 'John', 'Zara'}
Bob has friends Alice doesn’t have: True
'''
alice_friends = {"Sam", "Emma", "John", "Alice", "Zara"}
bob_friends = {"John", "Zara", "Lucas", "Mia"}

print(alice_friends.intersection(bob_friends))
print(alice_friends.difference(bob_friends))
print(alice_friends.union(bob_friends))

if bob_friends - alice_friends:
    print(True)
else:
    print(False)

#What is the output of the following code?
s1 = {1, 3, 5, 7, 9, 11}
s2 = {11, 22, 33}
s1.update(s2)
s2.add(44)
s1.remove(3)
print(f'{s1}\n{s2.intersection(s1)}')

'''
Object-Oriented Programming
1. Class: A blueprint for creating objects (a particular data structure) that describes what attributes and methods that are distinct type of object will have.

2. Object: An instance of a class. Create representations of real-life objects (e.g., a car, a dog, etc.) in code.
It is a collection of data (variables) and methods (functions) that operate on the data.

3. Attributes: Characteristics or properties of an object. They are defined in the class and can be accessed using the dot notation. (is/has)
ex. name, age, height, etc.

4. Methods: Functions defined inside a class that operate on the attributes of the class. They are called on objects of the class using the dot notation. (actions)
ex. eat, sleep, run, etc.
'''

class Car: # class names should be capitalized
    
    make = None # class attributes
    model = None
    year = None
    color = None

    def __init__(self, make, model, year, color): # constructor method (special method that is called when an object is created)
        self.make = make
        self.model = model
        self.year = year
        self.color = color 

    def drive(self): # methods (functions that belong to the class)
        print("The car is driving.")
    
    def stop(self): # methods (functions that belong to the class)
        print("The car has stopped.")

car_1 = Car("Toyota", "Camry", 2020, "Blue") # create an object of the class (instance of the class)

print(car_1.make) # access the attributes of the object using dot notation
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive() # call the methods of the object using dot notation
car_1.stop() # call the methods of the object using dot notation

class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    
    def calculate_area(self) -> int:
        self.area = self.width * self.length
        return self.area
    
    def __repr__(self) -> str: # USES print()
        return f'The rectangle with width {self.width} and length {self.length} has area {self.area}.'

rectangle1 = Rectangle(2, 3)
print(rectangle1.calculate_area())
print(rectangle1)

class Menu:
    def __init__(self):
        self.options = []
    
    def addOption(self, option: str) -> None:
        self.options.append(option)

    def getInput(self) -> str:
        done = False
        while not done:
            for i in range(len(self.options)):
                print(f'{i+1}) {self.options[i]}')
            try:
                user_choice = int(input('> '))
            except ValueError:
                print('Enter an integer value')
            else:
                if 1 <= user_choice < len(self.options):
                    done = True
        return self.options[user_choice - 1]
    
m1 = Menu()
m1.addOption('Drink')
m1.addOption('Side dish')
m1.addOption('Main dish')
m1.addOption('Dessert')
m1.addOption('Quit')
m1.getInput()
