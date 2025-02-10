'''What prints?'''

def numLoop():
    x = -5
    while x > -7:
        if x == -1:
            x = 50
            return x
    print(x)
    x = x + 1
    return 30

numLoop()