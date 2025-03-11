'''
Quetion 1: Create Pascal's Triangle more efficiently than O(n^3)-time and
O(n^2) space.  
'''
def pascal(num):
      lst1 = []
    
      for i in range(num):
            lst2 = [1]

            for j in range(1, i):
            # Use the recurrence relation: 
                  lst2.append(lst1[i-1][j-1] + lst1[i-1][j])
        
            if i > 0:
                  lst2.append(1)  # The last element of each row is always 1
        
            lst1.append(lst2)
    
      return lst1

print(pascal(2))
'''
Question 2: ToyBoxes
'''
# dont have the question
'''
Question 3: Baker Bonus
problem statement already online
'''
# DONE
'''
Question 4: Unique Paths
Given a m by n matrix, you are to determine and print the 
number of unique paths starting at the top left corner and
ending at the bottom right corner of the matrix.  The only
possible moves that can be made are either a move to the
right or down. 

Example-1: 

      0  1
[0   [x, x],
 1   [x, x]  ]

path 1: (0, 0) --> (0, 1) --> (1, 1)
path 2: (0, 0) --> (1, 0) --> (1, 1)

=> output: 2


Example-2: 

      0  1  2
[0   [x, x, x],
 1   [x, x, x],
 2   [x, x, x]  ]

path 1: (0, 0) --> (0, 1) --> (0, 2) --> (1, 2)
path 2: (0, 0) --> (0, 1) --> (1, 1) --> (1, 2)
path 3: (0, 0) --> (1, 0) --> (1, 1) --> (1, 2)

=> output: 3
'''
from math import factorial

def shortPath(n, m):
    path = n-1 + m-1
    path_count = factorial(path) // (factorial(n-1) * factorial(m-1))
    return path_count

a = int(input())
b = int(input())

print(shortPath(a, b))

'''
Question 5: 
Update Pascal's Triangle code so that your algorithm uses only O(1) space.
  
'''
def pascal(num):
      row = [1]
    
      for i in range(1, num):
            for j in range(i-1, 0, -1):
                  row[j] = row[j-1] + row[j]
        
            row.append(1)
    
      return row

print(pascal(100))

