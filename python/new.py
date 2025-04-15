def recursonfun(x):
    if x == 1:
        return 1
    else:
        return(x * (x-1))
    
num = int(input("Enter the number : "))
print("the factorail of ",num ," is " ,recursonfun(num))


