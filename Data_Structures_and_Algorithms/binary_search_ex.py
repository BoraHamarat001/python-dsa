def binary_search(numbers,target,L,H):
    if H<L:
        return False
    medium_index=(L+H)//2
    if numbers[medium_index]==target:
        return medium_index
    if numbers[medium_index] < target:
        return binary_search(numbers,target,medium_index+1,H) 
    else:
        return binary_search(numbers,target,L,medium_index-1)

def find_occurances(numbers,target,L,H):
    index=binary_search(numbers,target,L,H)
    indices=[index]
    i=index-1 
    while i>=0:
        if numbers[i]==target:
            indices.append(i)
        else:
            break 
        i=i-1 
        
    i=index+1
    while i<len(numbers):
        if numbers[i]==target:
            indices.append(i)
        else:
            break
        i+=1
    return sorted(indices)    