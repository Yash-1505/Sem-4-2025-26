a=int(input("1 = C to F\n2 = F to C\n"))
b=float(input("Enter the temperature "))
if a==1:
    F=(b*(9/5)+32)
    print(F)
elif a==2:
    c=(b-32)*(5/9)
    print(c)
else:
    print("Invalid input")