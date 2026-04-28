def jump_search(arr, target):
 
    data = {}
    data['arr'] = arr
    data['target'] = target
    n = len(arr)
    step = int(n ** 0.5)  # Calculate the optimal jump size

    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += step
        if prev >= n:
            data['index'] = -1 
            return data  # Target is not present in the array
 
    # Perform a linear search in the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            data['index'] = i 
            return data  # Target found at index i

    data['index'] = -1
    return data  # Target is not present in the array

 