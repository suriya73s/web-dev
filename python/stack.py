from collections import deque

stack = deque()
n=int(input("enter the number for inputs : "))
for i in range(n):
    stack.append(input("Enter the element : "))

print(f"\n initial stock : {stack}")

for i in range(n):
   print( stack.pop())

print(f"\ncurrent popped stack : {stack}")
     