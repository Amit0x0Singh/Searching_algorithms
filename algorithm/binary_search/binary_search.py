def binary_search(arr, target):
    
    data = {}
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            data['index'] = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if 'index' not in data:
        data['index'] = -1
    else:
        data['arr'] = arr
        data['target'] = target
        
    return data