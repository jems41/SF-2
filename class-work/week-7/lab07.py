'''
Question1:

Given a dictionary of keys that are strings and/or integers, 
values are lists, write a snippet of code that returns the total number
of elements of all lists that have keys as strings.  
'''

dict = {'apples': [1, 2], 41: [2, 3], 'pears': [4, 5], 'bananas': [6, 7]}

def elemStr(d):
    keys = list(d.keys())
    numElements = 0
    for key in keys:
        if type(key) == str:
            numElements += len(d[key])
    print(numElements)

#elemStr(dict)

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
def wordTally(n):
    repeats = {}
    for word in n:
        if word in repeats:
            repeats[word] += 1
        else:
            repeats[word] = 1

    return repeats

print(wordTally(['balls', 'balls', 'apple']))

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



'''
Question 4:

Given a sequence of m words and an integer k, find the
k-th most common words.  A word w is the k-th most 
common if exactly k-1 distinct words occur more
frequently than w. 
'''