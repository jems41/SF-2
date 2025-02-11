n, m, d = input().split()
n = int(n)
m = int(m)
d = int(d)
event_lst = list(map(int, input().split()))
if m != len(event_lst):
    print("INVALID!")

def isClean(n, m, d, event_lst):
    clean_shirts = n
    laundry_count = 0
    
    for i in range(1, d+1):
        if i in event_lst:
            clean_shirts += 1
        if clean_shirts == 0:
            clean_shirts = n
            laundry_count += 1
        clean_shirts -= 1

    return laundry_count   
        
print(isClean(n, m, d, event_lst))