import heapq as hq

liststu = []

n= int(input("Enter the number of students : "))

for i in range(n):
    roll = int(input("Enter the number: "))
    name = input("Enter the name: ")
    hq.heappush(liststu,(roll,name))
    
while liststu:
   roll,name =  hq.heappop(liststu)
   print(roll, " : ",name)