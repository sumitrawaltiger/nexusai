s=input("Enter any character")
if s.isalnum():
    print("It is alpha numeric character")
    if s.isalpha():
        print("It is alphabet symbol")
        if s.islower():
            print("It is lower  case alphabet symbol")
        else:
            print("It is upper case alphabet symbol")
    else:
        print("It is a digit")
elif s.isspace():
    print("It is space character")
else:
    print("It is non-space special character")