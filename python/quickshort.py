def shortfun(arr):
    if len(arr)<1:
        return arr
    
    pivot = arr[-1]
    
    right=[]
    left=[]
    middle=[]
    
    for i in arr:
        if i<pivot:
            right.append(i)
            
        elif i>pivot:
            left.append(i)
        else:
            middle.append(i)
    return shortfun(right)+middle+shortfun(left)

arr = list(map(int,input("Enter the element : ").split()))
print("unshorted array : ",arr)
print("Short array : ",shortfun(arr))
            
