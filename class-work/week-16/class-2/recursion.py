'''
reverse a string recursively
'''

def reverseString(s):
    if len(s) == 1:
        return s
    return s[-1] + reverseString(s[:-1])

s = 'hello'
print(reverseString(s))

def isSorted(lst):
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return isSorted(lst[1:])

lst = [1, 2, 3, 4, 5, 6, 7]
lst2 = [5, 2, 3, 4, 7, 8, 9]
lst3 = [2, 3, 4, 7, 5, 6, 9, 11, 12]
print(isSorted(lst))
print(isSorted(lst2))
print(isSorted(lst3))
print(isSorted([]))
print(isSorted([1]))
print(isSorted([5, 2]))
print(isSorted([7, 8, 2, 3, 6, 8]))
'''
Count the number of occurrences of a given
element in a list
'''
def countOccur(lst, target):
    pass
