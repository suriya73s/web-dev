arr = [8,9,2,3,4,56,77]
x= int(input("enter : "))
i=0
found = False

while i <len(arr):
    if arr[i] == x:
        print(f"elemetn present at the index of {i}")
        found = True
        break
    i +=1
    
if not found:
    print("element not found")  