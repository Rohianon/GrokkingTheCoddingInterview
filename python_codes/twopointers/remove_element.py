def remove_element(arr, key):
    next_element = 0; #index of the next element which is not key
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1
    return arr[:next_element]
