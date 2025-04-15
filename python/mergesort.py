def mersort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
        
    left = mersort(arr[:mid])
    right =mersort(arr[mid:]) 
        
    mersort(left)
    mersort(right)
        
    merged = []
    i=j=0
        
    while (i <len(left) and j < len(right)):
        if left[i] <right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
                
    merged += left[i:]
    merged += right[j:]
            
    return merged
        
arr = [3,4,1,32,5]
sorted = mersort(arr)
print("merged sordted array is : ",sorted)
