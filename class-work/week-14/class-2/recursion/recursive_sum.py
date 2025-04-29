def iterSum(n):
    total = 0
    for i in range(n):
        total += 1
    return total

def recSum(n):
    if n == 1:
        return 1
    else:
        return recSum(n-1) + n # function call
    
def recFactorial(n):
    if n == 1:
        return 1
    else:
        return recFactorial(n-1)
    
def badFibonacci(n):
    if n <= 1: # f0 = 0 and f1 = 1
        return n
    else:
        return badFibonacci(n-1) + badFibonacci(n-2)