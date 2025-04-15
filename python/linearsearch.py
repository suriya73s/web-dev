def search():
    numlist=list(map(int,input("Enter the number for list : ").split()))
    print("list is : ",numlist)
    key=int(input("enter hthe number : "))
    found = False
    i=0
    while i < len(numlist):
        if numlist[i] == key:
            print(f"the number {key} is available in {i} th index")
            found = True
            break
        i = i+1
        
    if not found:
        print("element not found")

search()