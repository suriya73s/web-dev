li = [2,34,5,67,23,6,5]

x = int(input("Enter the number : "))
i = 0

while i < len(li):
    if li[i] == x:
        print("THe element",x,"is present at ",i+1 ,"Position")
        break
    i += 1

if i>=len(li):
    print("Element is not present")