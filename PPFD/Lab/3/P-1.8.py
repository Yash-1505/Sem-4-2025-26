n=int(input("Provide the number of elements in the array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element: ")))
m=int(input("Enter 1 for Accending order and 2 for Descending order:  "))
if(m==1):
    arr.sort()
    print("The array in Accending order is:",arr)
elif(m==2):
    arr.sort(reverse=True)
    print("The array in Descending order is:",arr)
else:
    print("Invalid input")