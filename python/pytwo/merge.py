def mergesort(listy):
    
    if len(listy)<=1:
        return listy
    
    mid = len(listy)//2
    
    left = mergesort(listy[:mid])
    right = mergesort(listy[mid:])
    
    mergesort(left)
    mergesort(right)
    
    merged =[]
    i=j=0
    
    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j +=1
        
    merged += left[i:]
    merged +=right[j:]
        
    return merged
    
listy = [3,23,43,556,8]
print(mergesort(listy))