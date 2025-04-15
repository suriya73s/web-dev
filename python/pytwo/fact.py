def factorail(x):
    if x==1 or x==0:
        return 1
    else:
        return x * factorail(x-1)
    
x=int(input("enter the niber : "))
print(f"factorial of {x} ix ",factorail(x))