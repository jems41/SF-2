'''
Given a series of routes, find the roundabouts along a route and determine which route
has the smallest roundabout in diameter.  

INPUT SPECIFICATION:
Each route read from the user (a sequence of integers separated by a space) is:
--> first integer: ID for the given route
--> second integer R: number of roundabouts along the route
--> R integers follow which describe the diameter D of each roundabout along the route

OUTPUT SPECIFICATION:
the minimum roundabout diameter encountered along a route and which routes it appears on
--> e.g. 2 {1, 2, 3}


Sample Input-1
3
1 6 4 5 2 6 3 2
2 3 2 3 4
3 4 2 3 2 4

Sample Output-1
2 {1,2,3}

Sample Input-2
4
1 2 3 4
2 3 4 2 4
3 7 2 3 3 4 5 2 6
4 5 3 2 5 1 4

Sample Output-2
1 {4}
'''
# import math
num_routes = int(input('enter number of routes: '))
diameters_lst = []
min_diam = 70000
# min_diam = math.inf

for j in range(num_routes):     
    row = input(f'enter descritpion of route {j+1}: ').split()  
    for i in range(len(row)):  
        row[i] = int(row[i])
    id = row[0]     
    diam = row[1:-1]     
    current_diam = min(diam)   

    if current_diam < min_diam:
        min_diam = current_diam
        diameters_lst = [id]