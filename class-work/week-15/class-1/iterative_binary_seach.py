# I have a sorted list by splitting a list and finding

def binarySearch(lst, target):
    '''
    return the index of the target element in lst if present
    otherwise, return -1
    '''
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        mid = (low + mid)//2

        if lst[mid] < target:
            low = mid+1
        elif lst[mid] > target:
            high = mid-1
        else:
            return mid
    
    return -1

lst = [2, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 20]
elem = 5
print(binarySearch(lst, elem))