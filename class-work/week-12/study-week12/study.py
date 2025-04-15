'''
To study:
- map() function
- Dictionaries & Sets: week-6 to week-8 (sets: week-8)
    - creating dictionaries and sets
    - iterating through sets and dictionaries
    - dictionary operations, comparisons
    - comparing sets and set theoretic operations
    - mutable set operators and methods
    - nested dictionaries
    - dictionary and set comprehensions
- Read/Write files & exceptions: week-9 to week-10
    - standard files objects
    - text file processing: reading/writing/updating
    - remove/rename files
    - serialization with JSON
    - handling exceptions
    - try/except/else clause
- Object-Oriented Programming week-11 to week-12
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
    result = {} # d = {'Monarch': 5, 'Common Blue': 12} d['Monarch']
    for key in d1:
        for value in d1[key]:
            print(value)
            print(key.get(value))
            
    return result
                

print(combine2({'a': {3: [2], 4: [5, 6]}}, {'b': {3: [8, 12]}}))