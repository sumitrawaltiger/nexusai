# username=input("Enter user name")
# pwd = input("Enter password")
# if username.lower() =="durga" and pwd=="anushka":
#     print("Valid user")
# else:
#     print("Invalid user")
s=input("Enter any string").strip()
output = s[0].upper() + s[1:len(s)-1].lower() + s[-1].upper()
print(output)