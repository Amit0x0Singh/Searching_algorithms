def linear_search(arr, target):
    
    data ={}
    
    for index in range(len(arr)): 
        if arr[index] == target:
            data['index'] = index
            break
        
    if 'index' not in data:
        data['index'] = -1
    else :
        data['arr'] = arr
        data['target'] = target
        
    return data