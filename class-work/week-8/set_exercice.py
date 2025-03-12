'''
Firgus is behind on several assignments.
After rummaging through backpack, he realizes
he has N items, each of which he records as strings

He has M upcoming assignments, the i-th of which 
requestes T_i items to complete, r1, r2, ..., rT_i

If he has T_i required items, he can complete i-th
assignement. Otherwise, he flunks the i-th assignment.
How many assignment can firgus complete?

INPUT SPEC:

--> first line contains two integers N and M separated by
a space
--> next N line contains a single string s_i
    you can assume that the N strings are unique
--> next M sections contain a single integer T_i,
    followed by T_i lines each containing a single string

OUTPUT SPEC:
output the number of assignements

Sample input:
3 4
chalk
cheese
charger
1
cheese
2
coins
cash
3
charger
chalk
caffeine
3
cheese
charger
chalk

Sample Output:
2
'''

n, m = input().split()
n = int(n)
m = int(m)
s = set()
count = 0
for i in range(n):
    s.add(input())
for i in range(m):
    elems = int(input())
    assign = set()
    for j in range(elems):
        assign.add(input())
        if assign.issubset(s):
            count+=1

print(count)



