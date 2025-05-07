'''
bisect arguments:
-> lst to work  with
-> num to insert into the lst
-> [start, end] interval of lst to consider (defaulted to the entire lst)

bisect(lst, num, start, end)
returns index where num can be inserted so lst stays sorted
if num is already in lst, reutrn rightmost index where num can be inserted

bisect_left(lst, num start, end)
return the index where num can be inserted so lst stays sorted
if num is already in lst, returns the leftmost index where num can be inserted

bisert_right(lst, num, start, end)
same as bisect(...)
>>> bisect.bisect is bisect.bisect_right
>>> True
'''

import bisect
lst = [1, 2, 7, 7, 7, 8, 10, 11]
num = 7
print(bisect.bisect(lst, num)) # 5
print(bisect.bisect_left(lst, num)) # 2
print(bisect.bisect_right(lst, num)) # 5
