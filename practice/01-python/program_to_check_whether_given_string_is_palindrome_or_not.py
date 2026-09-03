s=input("Enter some string")
s=s.replace(" ","").lower()
if s==s[::-1]:
    print("Given string is palindrome")
else:
    print("Given string is not a palindrome")