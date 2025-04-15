list = list(map(int,input("enter the number to the list : ").split()))
x = int(input("enter the number to find"))
i=0
found = False
while i<len(list):
    if list[i]==x:
        print(f"the number {x} present at {i}th positoion")
        found = True
    i=i+1
    
if not found:
    print("element is not present")     

