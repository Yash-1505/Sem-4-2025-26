n=int(input("Enter number of values to enter into a list: "))
Li=[]
for i in range(n):
    val = float(input("Enter the value to the list: "))
    Li.append(val)

print(Li)
print((sum(Li)/len(Li)))