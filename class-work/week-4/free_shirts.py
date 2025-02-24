n, m, d = input().split()
n = int(n)
m = int(m)
d = int(d)
event_lst = list(map(int, input().split()))
if m != len(event_lst):
    print("INVALID!")

def isClean(n, d, event_lst):
    clean_shirts = n
    laundry_count = 0
    
    for day in range(1, d+1):
        if clean_shirts == 0:
            clean_shirts = n
            laundry_count += 1
        if day in event_lst:
            clean_shirts += 1
            n += 1
        clean_shirts -= 1

    return laundry_count   
        
print(isClean(n, d, event_lst))