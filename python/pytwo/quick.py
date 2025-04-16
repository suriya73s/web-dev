def qick(arr):
    if len(arr)<1:
        return arr
    
    pivot = arr[-1]
    
    left=[]
    right=[]
    middle=[]
    
    for i in arr:
        if i< pivot:
            left.append(i)
        elif i>pivot:
            right.append(i)
        else:
            middle.append(i)
    return qick(left)+middle+qick(right)

arr=[3,7,5,1,9,2]
print(qick(arr),end = "-")