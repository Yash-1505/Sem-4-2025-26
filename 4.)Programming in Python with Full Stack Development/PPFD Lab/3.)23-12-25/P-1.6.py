n=int(input("Enter the number for calculating factorial: "))
if(n<0):
    print("Factorial is not defined for negative and decimal numbers")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of %d is %d" %(n,fact))