def binarySearch(lst, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        
        if lst[mid] == target: # target found
            return mid
        elif lst[mid] < target: # search in right, ignoring left
            return binarySearch(lst, mid+1, high, target)
        else:
            return binarySearch(lst, low, mid-1, target)
    return -1

lst = [2, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 20]
elem = 5
print(binarySearch(lst, 0, len(lst)-1, elem))   