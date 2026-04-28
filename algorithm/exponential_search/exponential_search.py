def exponential_search(arr, target):
    data = {}
    data['arr'] = arr
    data['target'] = target
    n = len(arr)
    
    if n == 0:
        data['index'] = -1
        return data

    if arr[0] == target:
        data['index'] = 0
        return data

    index = 1
    while index < n and arr[index] < target:
        index *= 2

    left, right = index // 2, min(index, n - 1)

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            data['index'] = mid
            return data
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    data['index'] = -1
    return data