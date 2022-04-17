def binary_search(array, target):
    min_index, max_index = 0, len(array) - 1
    
    while min_index <= max_index:
        middle_index = (min_index + max_index) // 2
        
        if array[middle_index] < target:
            min_index = middle_index + 1
        elif array[middle_index] > target:
            max_index = middle_index - 1
        else:
            return middle_index
    return None