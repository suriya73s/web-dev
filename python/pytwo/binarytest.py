def binary(arr,low,high,x):
    if low>high:
        print("element notfound")
        return
    mid = (low+high)//2
    
    if arr[mid] == x:
        print(mid)
    elif arr[mid] < x:
        binary(arr,mid+1,high,x)
    else:
        binary(arr,low,mid-1,x)
    

arr = [6,4,67,8,23,9]
arr.sort()
x=6
binary(arr,0,len(arr)-1,x)

