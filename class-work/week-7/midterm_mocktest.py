def coordinates(n):
    grid = []
    for y in range(n):
        y_axis = []
        for x in range(n):
            t = (x, y)
            if n % 2 == 1 and x == y == n // 2:
                y_axis.append(" ** ")
            else:
                y_axis.append(t)
        grid.append(y_axis)
    return grid[::-1]

n = int(input())
result = coordinates(n)
for row in result:
    print(row)

def someFunction(n):
    lst = []
    for i in range(n):
        row = [j + 1 + i * n for j in range(n)]
        lst.append(row)
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for k in range(2, int(lst[i][j]**0.5) + 1):
                if lst[i][j] % k == 0:
                    lst[i][j] = 0
    return lst

modified = someFunction(5)
for row in modified:
    print(row)

