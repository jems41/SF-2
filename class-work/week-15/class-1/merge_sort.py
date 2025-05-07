def mergeSort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list
    