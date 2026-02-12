a=input("Enter the string to check if it is a palindrome: ")
if(a==a[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")