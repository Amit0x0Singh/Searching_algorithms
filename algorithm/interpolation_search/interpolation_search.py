def interpolation_search(arr, target):
   
    low = 0
    high = len(arr) - 1
    data = {}
    data['arr'] = arr
    data['target'] = target

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                data['index'] = low
                return data

            data['index'] = -1
            return data

        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])

        if pos < low or pos > high:
            data['index'] = -1
            return data

        if arr[pos] == target:
            data['index'] = pos
            return data
        
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    data['index'] = -1
    return data