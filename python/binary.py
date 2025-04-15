def binary(arr,low,high,x):
   
    if low >high:
        print("element is not found")
        return
    mid = (low+high)//2
    
    if arr[mid] == x:
        
        print(f"element {x} preasent st {mid} position")
        
    if arr[mid] > x:
        binary(arr,low,mid-1,x)
    elif arr[mid] < x:
        binary(arr,mid+1,high,x)

arr = list(map(int,input("Enter the elements  : ").split()))

arr = sorted(arr)
print(f"the list is : {arr}")
x = int(input("enter the elements ti find : "))

binary(arr,0,len(arr)-1,x)
        