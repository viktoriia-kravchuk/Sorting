def merge_sort(values):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    1. Divide step: find the midpoint of the list and divide into sublists
    2. Conquer step: recursively sort the sublists created in previous step
    3. Combine: merge thee sorted sublists created in previous step 

    """
    if len(values) <= 1:
        return values

    left_half, right_half = split(values)  
    left_values = merge_sort(left_half)
    right_values = merge_sort(right_half)

    return merge(left_values, right_values)


def split(values):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right 
    """
    middle_index = len(values) // 2
    left = values[:middle_index]
    right = values[middle_index:]
    return left, right

def merge(left_values, right_values):
    """
    Merges two lists(arrays), sorting them in the process
    Returns a new merged list
    """
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values


alist = [54,62,93,17,31,44,55,20]
l = merge_sort(alist)
print(l)